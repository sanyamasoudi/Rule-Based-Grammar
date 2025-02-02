from antlr4 import *
import argparse
from Code.AutoMLCodeGenerator import AutoMLCodeGenerator
from Code.AutoMLCustomListener import AutoMLCustomListener
from Repository.ast_to_networkx_graph import show_ast
from Repository.post_order_ast_traverser import PostOrderASTTraverser
from gen.AutoMLDSLLexer import AutoMLDSLLexer
from gen.AutoMLDSLParser import AutoMLDSLParser

def main(arguments):
	# load input
	stream = FileStream(arguments.input, encoding='utf8')
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

	show_ast(ast.root)

	post_order_ast_traverser = PostOrderASTTraverser()
	post_order_ast_traverser.node_attributes = ['label', 'text', 'number']
	traversal = post_order_ast_traverser.traverse_ast(ast.root)

	# print(traversal)

	code_generator = AutoMLCodeGenerator()
	generated_code = code_generator.generate_code(traversal)

	with open(arguments.output, 'w') as output_file:
		output_file.write(generated_code)

if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-i', '--input', help='Input source', default=r'example4_input.dsl')
	argparser.add_argument('-o', '--output', help='Output path', default=r'output.py')
	argparser.add_argument('--show-ast', action='store_true', help='Visualize the AST')
	args = argparser.parse_args()
	main(args)
