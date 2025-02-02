import os
from antlr4 import *
from Code.AutoMLCodeGenerator import AutoMLCodeGenerator
from Code.AutoMLCustomListener import AutoMLCustomListener
from Repository.post_order_ast_traverser import PostOrderASTTraverser
from gen.AutoMLDSLLexer import AutoMLDSLLexer
from gen.AutoMLDSLParser import AutoMLDSLParser

def run_test(input_file):
    stream = FileStream(input_file, encoding='utf8')
    lexer = AutoMLDSLLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = AutoMLDSLParser(token_stream)
    # convertino to parse tree
    parse_tree = parser.dsl()
    # convertion to AST
    ast_builder_listener = AutoMLCustomListener(parser.ruleNames)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_builder_listener)

    ast = ast_builder_listener.ast

    post_order_ast_traverser = PostOrderASTTraverser()
    post_order_ast_traverser.node_attributes = ['label', 'text', 'number']
    traversal = post_order_ast_traverser.traverse_ast(ast.root)

    # print(traversal)

    code_generator = AutoMLCodeGenerator()
    generated_code = code_generator.generate_code(traversal)

    return  generated_code

def main():
    test_cases = ["test_example_input1.dsl", "test_example_input2.dsl", "test_example_input3.dsl", "test_example_input4.dsl","test_example_input5.dsl", "test_example_input6.dsl", "test_example_input7.dsl", "test_example_input8.dsl",
                "test_example2_input1.dsl", "test_example2_input2.dsl", "test_example2_input3.dsl", "test_example2_input4.dsl","test_example2_input5.dsl", "test_example2_input6.dsl", "test_example2_input7.dsl", "test_example2_input8.dsl", "test_example2_input9.dsl",
                  "test_example3_input1.dsl","test_example3_input2.dsl"]
    for test_case in test_cases:
        generated_code = run_test(test_case)
        output_file = test_case.replace('.dsl', '_output.py')
        
        with open(output_file, 'w') as f:
            f.write(generated_code)
        
        print(f"Test case {test_case} executed successfully. Output written to {output_file}")

if __name__ == "__main__":
    main()
