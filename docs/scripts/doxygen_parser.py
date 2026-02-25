# Doxygen Parser

"""
This script parses Doxygen comments from source code files.
It extracts relevant information and presents it in a structured format.
"""

import re

# Function to parse Doxygen comments

def parse_doxygen_comments(source_code):
    """
    Parses the given source code and extracts Doxygen comments.

    :param source_code: str
    :return: list of extracted comments
    """
    # Regular expression to match Doxygen comments
    doxygen_pattern = re.compile(r'/\*\*[^*]*\*+([^/*][^*]*\*+/)')
    comments = doxygen_pattern.findall(source_code)
    return comments

# Example usage
if __name__ == '__main__':
    example_code = """
    /**
     * This is a sample Doxygen comment.
     * It describes the function's purpose.
     */
    void example_function() {}
    """
    extracted_comments = parse_doxygen_comments(example_code)
    print(extracted_comments)