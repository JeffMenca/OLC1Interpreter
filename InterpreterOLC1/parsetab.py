
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightUNOTleftMENORQUEMAYORQUEMAYORIGUALMENORIGUALDIFERENTEIGUALIGUALleftMASMENOSleftPORDIVMODnonassocPOTrightUMENOSAND BOOLEANO CADENA CHARACTER DECIMAL DECREMENTO DIFERENTE DIV ENTERO ID IGUAL IGUALIGUAL INCREMENTO LLAVEA LLAVEC MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MOD NOT OR PARA PARC POR POT PUNTOCOMA RBOOLEAN RBREAK RCASE RCHAR RCONTINUE RDEFAULT RDOUBLE RELSE RFOR RFUNC RIF RINT RLENGTH RMAIN RNULL RPRINT RREAD RRETURN RROUND RSTRING RSWITCH RTOLOWER RTOUPPER RTRUNCATE RTYPEOF RVAR RWHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr finins\n                        | declaracion_instr finins\n                        | declaracion2_instr finins\n                        | asignacion_instr finins\n                        | asignacion2_instr finins\n                        | if_instr\n                        | while_instr\n                        | break_instr finins\n                        | main_instr\n                        | funcion_instr\n                        | llamada_instr fininsfinins       : PUNTOCOMA\n                    | instruccion        : error PUNTOCOMAwhile_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVECbreak_instr     : RBREAK\n    imprimir_instr     : RPRINT PARA expresion PARC PUNTOCOMA\n    | RPRINT PARA expresion PARC \n    \n    declaracion_instr     : tipo ID IGUAL expresion\n    \n    declaracion2_instr     : tipo ID \n    \n    asignacion_instr     : ID IGUAL expresion\n    \n    asignacion2_instr     : ID expresion\n    if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instrmain_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVECfuncion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVECllamada_instr     : ID PARA PARCtipo     : RINT\n                | RDOUBLE\n                | RCHAR\n                | RSTRING\n                | RVAR\n                | RBOOLEAN \n    expresion : expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion POR expresion\n            | expresion DIV expresion\n            | expresion POT expresion\n            | expresion MOD expresion\n            | expresion MENORQUE expresion\n            | expresion MAYORQUE expresion\n            | expresion MENORIGUAL expresion\n            | expresion MAYORIGUAL expresion\n            | expresion DIFERENTE expresion\n            | expresion IGUALIGUAL expresion\n            | expresion AND expresion\n            | expresion OR expresion\n            | expresion INCREMENTO\n            | expresion DECREMENTO\n    \n    expresion : MENOS expresion %prec UMENOS \n            | NOT expresion %prec UNOT \n    \n    expresion :   PARA expresion PARC \n    expresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : CHARACTERexpresion : BOOLEANOexpresion : RNULLexpresion : INCREMENTOexpresion : DECREMENTO'
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[15,15,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,15,-20,15,15,15,15,15,15,-29,15,-26,-18,-30,15,-28,15,-27,]),'RPRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[16,16,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,16,-20,16,16,16,16,16,16,-29,16,-26,-18,-30,16,-28,16,-27,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,18,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[18,18,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,41,42,-19,59,-32,-33,-34,-35,-36,-37,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,42,-23,-57,42,-25,42,42,-64,-65,42,-58,-59,-60,-61,-62,-63,42,42,42,42,-24,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,18,-20,18,18,18,18,18,18,-29,18,-26,-18,-30,18,-28,18,-27,]),'RIF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,],[19,19,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,19,-20,19,19,19,19,19,19,-29,19,-26,-18,-30,19,19,-28,19,-27,]),'RWHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[20,20,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,20,-20,20,20,20,20,20,20,-29,20,-26,-18,-30,20,-28,20,-27,]),'RBREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[21,21,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,21,-20,21,21,21,21,21,21,-29,21,-26,-18,-30,21,-28,21,-27,]),'RMAIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[22,22,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,22,-20,22,22,22,22,22,22,-29,22,-26,-18,-30,22,-28,22,-27,]),'RFUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[23,23,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,23,-20,23,23,23,23,23,23,-29,23,-26,-18,-30,23,-28,23,-27,]),'RINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[24,24,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,24,-20,24,24,24,24,24,24,-29,24,-26,-18,-30,24,-28,24,-27,]),'RDOUBLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[25,25,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,25,-20,25,25,25,25,25,25,-29,25,-26,-18,-30,25,-28,25,-27,]),'RCHAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[26,26,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,26,-20,26,26,26,26,26,26,-29,26,-26,-18,-30,26,-28,26,-27,]),'RSTRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[27,27,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,27,-20,27,27,27,27,27,27,-29,27,-26,-18,-30,27,-28,27,-27,]),'RVAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[28,28,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,28,-20,28,28,28,28,28,28,-29,28,-26,-18,-30,28,-28,28,-27,]),'RBOOLEAN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,107,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,],[29,29,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,29,-20,29,29,29,29,29,29,-29,29,-26,-18,-30,29,-28,29,-27,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,109,116,118,119,120,123,125,],[0,-1,-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,-20,-29,-26,-18,-30,-28,-27,]),'LLAVEC':([3,4,5,6,7,8,9,10,11,12,13,14,21,30,31,32,33,34,35,36,37,38,39,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,109,112,114,115,116,117,118,119,120,123,124,125,],[-3,-16,-16,-16,-16,-16,-9,-10,-16,-12,-13,-16,-19,-2,-4,-15,-5,-6,-7,-8,-11,-14,-17,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,-21,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,-20,116,118,119,-29,120,-26,-18,-30,-28,125,-27,]),'PUNTOCOMA':([4,5,6,7,8,11,14,15,21,41,42,44,47,48,50,51,52,53,54,55,63,78,79,80,82,83,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,109,],[32,32,32,32,32,32,32,39,-19,-23,-57,-25,-64,-65,-58,-59,-60,-61,-62,-63,-24,-52,-53,-31,-54,-55,109,-22,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,-20,]),'PARA':([16,18,19,20,22,40,43,45,46,49,56,57,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[40,45,56,57,58,60,60,60,60,60,60,60,87,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'IGUAL':([18,41,],[43,62,]),'MENOS':([18,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[46,46,-57,46,65,46,46,-64,-65,46,-58,-59,-60,-61,-62,-63,46,46,46,65,46,65,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-52,-53,65,-54,65,65,65,65,-38,-39,-40,-41,-42,-43,65,65,65,65,65,65,65,65,-56,]),'NOT':([18,40,43,45,46,49,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'ENTERO':([18,40,43,45,46,49,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'DECIMAL':([18,40,43,45,46,49,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'CADENA':([18,40,43,45,46,49,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'CHARACTER':([18,40,43,45,46,49,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'BOOLEANO':([18,40,43,45,46,49,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'RNULL':([18,40,43,45,46,49,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'INCREMENTO':([18,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[47,47,-57,47,78,47,47,-64,-65,47,-58,-59,-60,-61,-62,-63,47,47,47,78,47,78,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-52,-53,78,-54,-55,78,78,78,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,]),'DECREMENTO':([18,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[48,48,-57,48,79,48,48,-64,-65,48,-58,-59,-60,-61,-62,-63,48,48,48,79,48,79,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-52,-53,79,-54,-55,79,79,79,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,]),'MAS':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,64,-64,-65,-58,-59,-60,-61,-62,-63,64,64,-52,-53,64,-54,64,64,64,64,-38,-39,-40,-41,-42,-43,64,64,64,64,64,64,64,64,-56,]),'POR':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,66,-64,-65,-58,-59,-60,-61,-62,-63,66,66,-52,-53,66,-54,66,66,66,66,66,66,-40,-41,-42,-43,66,66,66,66,66,66,66,66,-56,]),'DIV':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,67,-64,-65,-58,-59,-60,-61,-62,-63,67,67,-52,-53,67,-54,67,67,67,67,67,67,-40,-41,-42,-43,67,67,67,67,67,67,67,67,-56,]),'POT':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,68,-64,-65,-58,-59,-60,-61,-62,-63,68,68,-52,-53,68,-54,68,68,68,68,68,68,68,68,None,68,68,68,68,68,68,68,68,68,-56,]),'MOD':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,69,-64,-65,-58,-59,-60,-61,-62,-63,69,69,-52,-53,69,-54,69,69,69,69,69,69,-40,-41,-42,-43,69,69,69,69,69,69,69,69,-56,]),'MENORQUE':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,70,-64,-65,-58,-59,-60,-61,-62,-63,70,70,-52,-53,70,-54,70,70,70,70,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,70,70,-56,]),'MAYORQUE':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,71,-64,-65,-58,-59,-60,-61,-62,-63,71,71,-52,-53,71,-54,71,71,71,71,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,71,71,-56,]),'MENORIGUAL':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,72,-64,-65,-58,-59,-60,-61,-62,-63,72,72,-52,-53,72,-54,72,72,72,72,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,72,72,-56,]),'MAYORIGUAL':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,73,-64,-65,-58,-59,-60,-61,-62,-63,73,73,-52,-53,73,-54,73,73,73,73,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,73,73,-56,]),'DIFERENTE':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,74,-64,-65,-58,-59,-60,-61,-62,-63,74,74,-52,-53,74,-54,74,74,74,74,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,74,74,-56,]),'IGUALIGUAL':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,75,-64,-65,-58,-59,-60,-61,-62,-63,75,75,-52,-53,75,-54,75,75,75,75,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,75,75,-56,]),'AND':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,76,-64,-65,-58,-59,-60,-61,-62,-63,76,76,-52,-53,76,-54,-55,76,76,76,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,76,-56,]),'OR':([42,44,47,48,50,51,52,53,54,55,61,63,78,79,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,77,-64,-65,-58,-59,-60,-61,-62,-63,77,77,-52,-53,77,-54,-55,77,77,77,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,]),'PARC':([42,45,47,48,50,51,52,53,54,55,58,61,78,79,81,82,83,84,85,87,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,],[-57,80,-64,-65,-58,-59,-60,-61,-62,-63,86,88,-52,-53,104,-54,-55,105,106,108,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-56,]),'LLAVEA':([86,105,106,108,121,],[107,110,111,113,122,]),'RELSE':([118,],[121,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,107,110,111,113,122,],[2,112,114,115,117,124,]),'instruccion':([0,2,107,110,111,112,113,114,115,117,122,124,],[3,30,3,3,3,30,3,30,30,30,3,30,]),'imprimir_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'declaracion_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'declaracion2_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'asignacion_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'asignacion2_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'if_instr':([0,2,107,110,111,112,113,114,115,117,121,122,124,],[9,9,9,9,9,9,9,9,9,9,123,9,9,]),'while_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'break_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'main_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'funcion_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'llamada_instr':([0,2,107,110,111,112,113,114,115,117,122,124,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'tipo':([0,2,107,110,111,112,113,114,115,117,122,124,],[17,17,17,17,17,17,17,17,17,17,17,17,]),'finins':([4,5,6,7,8,11,14,],[31,33,34,35,36,37,38,]),'expresion':([18,40,43,45,46,49,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[44,61,63,81,82,83,84,85,81,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',244),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',249),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',258),
  ('instruccion -> imprimir_instr finins','instruccion',2,'p_instruccion','grammar.py',267),
  ('instruccion -> declaracion_instr finins','instruccion',2,'p_instruccion','grammar.py',268),
  ('instruccion -> declaracion2_instr finins','instruccion',2,'p_instruccion','grammar.py',269),
  ('instruccion -> asignacion_instr finins','instruccion',2,'p_instruccion','grammar.py',270),
  ('instruccion -> asignacion2_instr finins','instruccion',2,'p_instruccion','grammar.py',271),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','grammar.py',272),
  ('instruccion -> while_instr','instruccion',1,'p_instruccion','grammar.py',273),
  ('instruccion -> break_instr finins','instruccion',2,'p_instruccion','grammar.py',274),
  ('instruccion -> main_instr','instruccion',1,'p_instruccion','grammar.py',275),
  ('instruccion -> funcion_instr','instruccion',1,'p_instruccion','grammar.py',276),
  ('instruccion -> llamada_instr finins','instruccion',2,'p_instruccion','grammar.py',277),
  ('finins -> PUNTOCOMA','finins',1,'p_finins','grammar.py',281),
  ('finins -> <empty>','finins',0,'p_finins','grammar.py',282),
  ('instruccion -> error PUNTOCOMA','instruccion',2,'p_instruccion_error','grammar.py',286),
  ('while_instr -> RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC','while_instr',7,'p_while','grammar.py',293),
  ('break_instr -> RBREAK','break_instr',1,'p_break','grammar.py',299),
  ('imprimir_instr -> RPRINT PARA expresion PARC PUNTOCOMA','imprimir_instr',5,'p_imprimir','grammar.py',306),
  ('imprimir_instr -> RPRINT PARA expresion PARC','imprimir_instr',4,'p_imprimir','grammar.py',307),
  ('declaracion_instr -> tipo ID IGUAL expresion','declaracion_instr',4,'p_declaracion','grammar.py',315),
  ('declaracion2_instr -> tipo ID','declaracion2_instr',2,'p_declaracion2','grammar.py',323),
  ('asignacion_instr -> ID IGUAL expresion','asignacion_instr',3,'p_asignacion','grammar.py',331),
  ('asignacion2_instr -> ID expresion','asignacion2_instr',2,'p_asignacion2','grammar.py',337),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC','if_instr',7,'p_if1','grammar.py',344),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC','if_instr',11,'p_if2','grammar.py',348),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr','if_instr',9,'p_if3','grammar.py',352),
  ('main_instr -> RMAIN PARA PARC LLAVEA instrucciones LLAVEC','main_instr',6,'p_main','grammar.py',358),
  ('funcion_instr -> RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC','funcion_instr',7,'p_funcion','grammar.py',364),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada','grammar.py',370),
  ('tipo -> RINT','tipo',1,'p_tipo','grammar.py',376),
  ('tipo -> RDOUBLE','tipo',1,'p_tipo','grammar.py',377),
  ('tipo -> RCHAR','tipo',1,'p_tipo','grammar.py',378),
  ('tipo -> RSTRING','tipo',1,'p_tipo','grammar.py',379),
  ('tipo -> RVAR','tipo',1,'p_tipo','grammar.py',380),
  ('tipo -> RBOOLEAN','tipo',1,'p_tipo','grammar.py',381),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','grammar.py',400),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','grammar.py',401),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',402),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','grammar.py',403),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','grammar.py',404),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion_binaria','grammar.py',405),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',406),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',407),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',408),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',409),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria','grammar.py',410),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',411),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','grammar.py',412),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','grammar.py',413),
  ('expresion -> expresion INCREMENTO','expresion',2,'p_expresion_binaria','grammar.py',414),
  ('expresion -> expresion DECREMENTO','expresion',2,'p_expresion_binaria','grammar.py',415),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','grammar.py',463),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','grammar.py',464),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion_agrupacion','grammar.py',476),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','grammar.py',482),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','grammar.py',486),
  ('expresion -> DECIMAL','expresion',1,'p_primitivo_decimal','grammar.py',491),
  ('expresion -> CADENA','expresion',1,'p_primitivo_cadena','grammar.py',496),
  ('expresion -> CHARACTER','expresion',1,'p_primitivo_character','grammar.py',501),
  ('expresion -> BOOLEANO','expresion',1,'p_primitivo_booleano','grammar.py',506),
  ('expresion -> RNULL','expresion',1,'p_primitivo_null','grammar.py',510),
  ('expresion -> INCREMENTO','expresion',1,'p_primitivo_incremento','grammar.py',514),
  ('expresion -> DECREMENTO','expresion',1,'p_primitivo_decremento','grammar.py',518),
]
