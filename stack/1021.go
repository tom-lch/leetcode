package stack

func removeOuterParentheses(S string) string {
	//var start, index int = 0, 0
	start, index := 0, 0
	s := ""
	for n, i := range S {
		if (i == '(') {
			start++
		}
		if (i == ')') {
			start--
		}
		if (i == '(' && start == 1) {
			index = n
		}
		if (start == 0) {
			s += S[index+1:n]
		}
	}
	return s
}
