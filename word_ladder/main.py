class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if start == end:
            return 1

        all_chars = map(chr, xrange(ord('a'), ord('z') + 1))
        visited = set()
        bfs = [start, None]

        # at which distance the following to-be-processed nodes are
        distance = 2

        while len(bfs) > 1:
            word = bfs.pop(0)
            if word is None:
                distance += 1
                bfs.append(None)
                continue

            for i in xrange(len(word)):
                for char in all_chars:
                    new_word = word[:i] + char + word[i + 1:]
                    if new_word == end:
                        return distance
                    if new_word in dict and new_word not in visited:
                        bfs.append(new_word)
                        visited.add(new_word)

        return 0
        


def main():  
    s = Solution()
    print s.ladderLength("hit","cog",["hot","dot","dog","lot","log"])
    a2 = "qa"
    b2 = "sq"
    d2 = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    print s.ladderLength(a2,b2,d2)
    


if __name__ == "__main__":
    main()