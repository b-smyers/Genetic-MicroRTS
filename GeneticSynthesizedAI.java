package ai.genetic;

import ai.core.AIWithComputationBudget;
import ai.synthesis.dslForScriptGenerator.DSLCommandInterfaces.ICommand;
import ai.synthesis.dslForScriptGenerator.DSLCompiler.MainDSLCompiler;
import ai.synthesis.dslForScriptGenerator.DslAI;
import ai.synthesis.grammar.dslTree.utils.ReduceDSLController;
import ai.synthesis.runners.cleanAST.TradutorDSL;
import ai.core.AI;
import ai.core.ParameterSpecification;
import ai.synthesis.grammar.dslTree.interfacesDSL.iDSL;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import rts.GameState;
import rts.PlayerAction;
import rts.units.UnitTypeTable;
import ai.synthesis.dslForScriptGenerator.DSLCompiler.IDSLCompiler;

public class GeneticSynthesizedAI extends AIWithComputationBudget {

    UnitTypeTable utt;
    String script = "for(u) ( build(Base,2,Up,u) harvest(10,u) attack(Worker,random,u) attack(Worker,mostHealthy,u) moveToUnit(Ranged,Enemy,closest,u) build(Barrack,13,Left,u) train(Worker,7,Right,u) harvest(18,u) moveToCoord(Heavy,13,14,u) moveToCoord(Ranged,13,10,u) moveaway(Heavy,u) build(Barrack,20,Down,u) if(!HaveQtdUnitsbyType(Light,12)) then( moveToCoord(Heavy,8,6,u) )) if(!HaveUnitsinEnemyRange(Heavy))  moveToUnit(Heavy,Ally,strongest) if(!HaveQtdUnitsAttacking(Heavy,4))";

    AI ai;

    public GeneticSynthesizedAI(UnitTypeTable utt) {
        super(-1,-1); // timeBudget = -1, iterationsBudget = -1
        this.utt = utt;

        // Translate script to Domain Specific Language (DSL)
        TradutorDSL DSL = new TradutorDSL(script);
        // Get Abstract Syntax Tree (AST) of DSL
        iDSL rec = DSL.getAST();
        // Create new DSL AI object
        this.ai = buildCommandsAI(utt, rec);
        // Prune out unactivated code
        ReduceDSLController.removeUnactivatedParts(rec, new ArrayList<>(((DslAI) ai).getCommands()));
        // print
        System.out.println(rec.translate());
    }

    @Override
    public void reset() {
        ai.reset();
    }

    @Override
    public AI clone() {
        return new GeneticSynthesizedAI(utt);
    }

    @Override
    public PlayerAction getAction(int player, GameState gs) throws Exception {
        return ai.getAction(player, gs);
    }

    private static AI buildCommandsAI(UnitTypeTable utt, iDSL code) {
        IDSLCompiler compiler = new MainDSLCompiler();
        HashMap<Long, String> counterByFunction = new HashMap<Long, String>();
        List<ICommand> commandsDSL = compiler.CompilerCode(code, utt);
        return new DslAI(utt, commandsDSL, "P1", code, counterByFunction);
    }

    @Override
    public List<ParameterSpecification> getParameters()
    {
        return new ArrayList<>();
    }

}