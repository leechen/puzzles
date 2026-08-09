import pytest

from python.common import Interval, ListNode, TreeNode


def tree():
    return TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))


def linked_values(head):
    result = []
    while head: result.append(head.val); head = head.next
    return result


def array_car_fleet():
    from python.array.car_fleet import CarFleet
    solution = CarFleet(); assert solution.car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3; assert solution.car_fleet(10, [], []) == 0


def array_encode_decode():
    from python.array.encode_decode import Codec
    codec = Codec()
    for values in ([], [""], ["a#b", "雪"]): assert codec.decode(codec.encode(values)) == values


def array_group_anagram():
    from python.array.group_anagram import GroupAnagrams
    groups = GroupAnagrams().group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert {frozenset(group) for group in groups} == {frozenset({"eat", "tea", "ate"}), frozenset({"tan", "nat"}), frozenset({"bat"})}


def array_longest_consecutive():
    from python.array.longest_consecutive import LongestConsecutive
    solution = LongestConsecutive(); assert solution.longest_consecutive([100, 4, 200, 1, 3, 2]) == 4; assert solution.longest_consecutive([]) == 0


def array_product_except_self():
    from python.array.product_except_self import ProductExceptSelf
    solution = ProductExceptSelf(); assert solution.product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]; assert solution.product_except_self([]) == []


def array_spiral_order():
    from python.array.spiral_order import SpiralOrder
    solution = SpiralOrder(); matrix = [[1,2,3],[4,5,6],[7,8,9]]
    assert solution.spiral_order(matrix) == [1,2,3,6,9,8,7,4,5]; assert solution.spiral_order_iterative(matrix) == solution.spiral_order(matrix); assert solution.spiral_order([]) == []


def array_top_k_elements():
    from python.array.top_k_elements import TopKFrequent
    assert TopKFrequent().top_k_frequent([1,1,1,2,2,3], 2) == [1,2]


def array_two_sum():
    from python.array.two_sum import TwoSum
    solution = TwoSum(); assert solution.two_sum([2,7,11,15], 9) == [0,1]; assert solution.two_sum([1], 2) is None


def array_valid_sudoku():
    from python.array.valid_sudoku import ValidSudoku
    board = [list("53..7...."),list("6..195..."),list(".98....6."),list("8...6...3"),list("4..8.3..1"),list("7...2...6"),list(".6....28."),list("...419..5"),list("....8..79")]
    solution = ValidSudoku(); assert solution.is_valid_sudoku(board); board[0][1] = "5"; assert not solution.is_valid_sudoku(board)


def backtrack_permute():
    from python.backtrack.permute import Permutations
    solution = Permutations(); expected = {(1,2),(2,1)}
    assert {tuple(x) for x in solution.permute([1,2])} == expected; values=[1,2]; assert {tuple(x) for x in solution.permute_recursive(values)} == expected; assert values == [1,2]


def backtrack_phone_character():
    from python.backtrack.phone_character import LetterCombinations
    solution = LetterCombinations(); assert solution.letter_combinations("23")[:3] == ["ad","ae","af"]; assert len(solution.letter_combinations("79")) == 16; assert solution.letter_combinations("") == []


def backtrack_power_subset():
    from python.backtrack.power_subset import Subsets
    assert {tuple(x) for x in Subsets().subsets([1,2])} == {(),(1,),(2,),(1,2)}


def backtrack_subarray_sum():
    from python.backtrack.subarray_sum import CombinationSum
    solution = CombinationSum(); assert {tuple(x) for x in solution.combination_sum([2,3,6,7],7)} == {(2,2,3),(7,)}; assert solution.combination_sum([2],1) == []


def dynamic_programming_regex_parse():
    from python.dynamic_programming.regex_parse import RegexMatcher
    solution = RegexMatcher(); assert solution.is_match("aa","a*"); assert solution.is_match("ab",".*"); assert not solution.is_match("ab",".*c")


def graph_can_finish_courses():
    from python.graph.can_finish_courses import CourseSchedule
    solution=CourseSchedule(); assert solution.can_finish(2,[[1,0]]); assert not solution.can_finish(2,[[1,0],[0,1]]); assert solution.can_finish(0,[])


def graph_capture():
    from python.graph.capture import SurroundedRegions
    board=[list("XXXX"),list("XOOX"),list("XXOX"),list("XOXX")]; SurroundedRegions().solve(board); assert ["".join(x) for x in board] == ["XXXX","XXXX","XXXX","XOXX"]
    empty=[]; SurroundedRegions().solve(empty); assert empty == []


def graph_clone_graph():
    from python.graph.clone_graph import CloneGraph, GraphNode
    a,b=GraphNode(1),GraphNode(2); a.neighbors=[b]; b.neighbors=[a]; solution=CloneGraph(); cloned=solution.clone_graph(a)
    assert cloned is not a and cloned.val==1 and cloned.neighbors[0] is not b and cloned.neighbors[0].neighbors[0] is cloned; assert solution.clone_graph(None) is None; assert solution.clone_graph(a) is not cloned


def graph_course_schedule_2():
    from python.graph.course_schedule_2 import CourseOrder
    solution=CourseOrder(); assert solution.find_order(2,[[1,0]]) == [0,1]; assert solution.find_order(2,[[1,0],[0,1]]) == []; assert solution.find_order(0,[]) == []


def graph_generate_parenthesis():
    from python.graph.generate_parenthesis import GenerateParentheses
    solution=GenerateParentheses(); assert set(solution.generate_parenthesis(3)) == {"((()))","(()())","(())()","()(())","()()()"}; assert solution.generate_parenthesis(0)==[""]


def graph_graph_is_tree():
    from python.graph.graph_is_tree import ValidTree
    solution=ValidTree(); assert solution.valid_tree(5,[[0,1],[0,2],[0,3],[1,4]]); assert not solution.valid_tree(4,[[0,1],[2,3]]); assert solution.valid_tree(0,[])


def graph_max_area_of_islands():
    from python.graph.max_area_of_islands import MaxAreaOfIsland
    solution=MaxAreaOfIsland(); assert solution.max_area_of_island([[1,1,0],[1,0,1]]) == 3; assert solution.max_area_of_island([])==0; assert solution.max_area_of_island([[0]])==0


def graph_maze():
    from python.graph.maze import Maze
    solution=Maze(); maze=[[0,0,1],[1,0,0]]; assert solution.has_path(maze,[0,0],[1,2]); assert not solution.has_path(maze,[0,0],[1,0]); assert not solution.has_path([], [0,0],[0,0])


def graph_num_of_islands():
    from python.graph.num_of_islands import NumberOfIslands
    solution=NumberOfIslands(); assert solution.num_islands([list("110"),list("010"),list("001")]) == 2; assert solution.num_islands([])==0


def graph_role_checker():
    from python.graph.role_checker import RoleChecker, RoleRelation
    checker=RoleChecker([RoleRelation(4,2),RoleRelation(2,0),RoleRelation(4,3)]); checker.assign([4]); assert checker.has_role(4); assert checker.has_role(0); assert not checker.has_role(5); checker.assign([3]); assert not checker.has_role(2)


def graph_rotten_orange():
    from python.graph.rotten_orange import RottenOranges
    solution=RottenOranges(); assert solution.oranges_rotting([[2,1,1],[1,1,0],[0,1,1]])==4; assert solution.oranges_rotting([[2,1,1],[0,1,1],[1,0,1]])==-1; assert solution.oranges_rotting([])==0; assert solution.oranges_rotting([[0]])==0


def greedy_jump():
    from python.greedy.jump import JumpGame
    solution=JumpGame(); assert solution.can_jump([2,3,1,1,4]); assert not solution.can_jump([3,2,1,0,4]); assert solution.can_jump([0])


def greedy_max_subarray_sum():
    from python.greedy.max_subarray_sum import MaximumSubarray
    solution=MaximumSubarray(); assert solution.max_subarray([-2,1,-3,4,-1,2,1,-5,4])==6; assert solution.max_subarray([-3])==-3; assert solution.max_subarray([])==0


def heap_kth_largest():
    from python.heap.kth_largest import KthLargest
    stream=KthLargest(3,[4,5,8,2]); assert [stream.add(x) for x in [3,5,10,9,4]] == [4,5,5,8,8]
    with pytest.raises(ValueError): KthLargest(0,[])


def heap_median_of_stream():
    from python.heap.median_of_stream import MedianFinder
    finder=MedianFinder()
    with pytest.raises(ValueError): finder.find_median()
    finder.add_num(1); assert finder.find_median()==1; finder.add_num(2); assert finder.find_median()==1.5; finder.add_num(3); assert finder.find_median()==2


def interval_meeting_room():
    from python.interval.meeting_room import MeetingRooms
    solution=MeetingRooms(); assert solution.can_attend_meetings([Interval(0,5),Interval(5,7)]); assert not solution.can_attend_meetings([Interval(0,6),Interval(5,7)]); assert solution.can_attend_meetings([])


def interval_meeting_room_2():
    from python.interval.meeting_room_2 import MinimumMeetingRooms
    solution=MinimumMeetingRooms(); assert solution.min_meeting_rooms([Interval(0,30),Interval(5,10),Interval(15,20)])==2; assert solution.min_meeting_rooms([])==0; assert solution.min_meeting_rooms([Interval(0,1),Interval(1,2)])==1


def interval_non_overlapping():
    from python.interval.non_overlapping import NonOverlappingIntervals
    solution=NonOverlappingIntervals(); assert solution.erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])==1; assert solution.erase_overlap_intervals([])==0


def linked_list_lru_cache():
    from python.linked_list.lru_cache import LRUCache
    cache=LRUCache(2); cache.put(1,1); cache.put(2,2); assert cache.get(1)==1; cache.put(3,3); assert cache.get(2)==-1; cache.put(1,10); assert cache.get(1)==10
    with pytest.raises(ValueError): LRUCache(0)


def linked_list_reorder():
    from python.linked_list.reorder import ReorderList
    head=ListNode(1,ListNode(2,ListNode(3,ListNode(4)))); solution=ReorderList(); solution.reorder_list(head); assert linked_values(head)==[1,4,2,3]; solution.reorder_list(None)


def linked_list_reverse_list():
    from python.linked_list.reverse_list import ReverseList
    solution=ReverseList(); assert linked_values(solution.reverse_list(ListNode(1,ListNode(2,ListNode(3)))))==[3,2,1]; assert linked_values(solution.reverse_list_recursive(ListNode(1,ListNode(2))))==[2,1]; assert solution.reverse_list(None) is None


def search_binary_search():
    from python.search.binary_search import BinarySearch
    solution=BinarySearch(); assert solution.search([-1,0,3,5,9,12],9)==4; assert solution.search([1],2)==-1; assert solution.search([],1)==-1


def search_koko_eat_banana():
    from python.search.koko_eat_banana import KokoEatingBananas
    solution=KokoEatingBananas(); assert solution.min_eating_speed([3,6,7,11],8)==4; assert solution.min_eating_speed([30,11,23,4,20],5)==30; assert solution.min_eating_speed([],1)==0


def search_search_in_rotated_array():
    from python.search.search_in_rotated_array import RotatedArraySearch
    solution=RotatedArraySearch(); values=[4,5,6,7,0,1,2]; assert solution.search(values,0)==4; assert solution.search(values,6)==2; assert solution.search(values,3)==-1; assert solution.search([],1)==-1


def search_search_matrix():
    from python.search.search_matrix import MatrixSearch
    solution=MatrixSearch(); matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert solution.search_matrix(matrix,3); assert not solution.search_matrix(matrix,13); assert solution.search_matrix_two_phase(matrix,60); assert not solution.search_matrix([],1)


def search_time_map():
    from python.search.time_map import TimeMap
    values=TimeMap(); values.set("foo","bar",1); assert values.get("foo",1)=="bar"; assert values.get("foo",3)=="bar"; assert values.get("foo",0)==""; assert values.get("missing",9)==""; values.set("foo","bar2",4); assert values.get("foo",4)=="bar2"


def stack_brackets():
    from python.stack.brackets import ValidBrackets
    solution=ValidBrackets(); assert solution.is_valid("()[]{}"); assert not solution.is_valid("(]"); assert not solution.is_valid("("); assert solution.is_valid("")


def stack_daily_temperatures():
    from python.stack.daily_temperatures import DailyTemperatures
    solution=DailyTemperatures(); assert solution.daily_temperatures([73,74,75,71,69,72,76,73])==[1,1,4,2,1,1,0,0]; assert solution.daily_temperatures([])==[]


def stack_min_stack():
    from python.stack.min_stack import MinStack
    stack=MinStack(); stack.pop(); stack.push(-2); stack.push(0); stack.push(-3); assert stack.get_min()==-3; stack.pop(); assert stack.top()==0 and stack.get_min()==-2
    empty=MinStack()
    with pytest.raises(IndexError): empty.top()
    with pytest.raises(IndexError): empty.get_min()


def tree_binary_tree_right_view():
    from python.tree.binary_tree_right_view import RightSideView
    solution=RightSideView(); assert solution.right_side_view(tree())==[4,6,7]; assert solution.right_side_view(None)==[]


def tree_construct_bst():
    from python.tree.construct_bst import BuildTree
    solution=BuildTree(); root=solution.build_tree([3,9,20,15,7],[9,3,15,20,7]); assert root.val==3 and root.left.val==9 and root.right.left.val==15; assert solution.build_tree([],[]) is None
    with pytest.raises(ValueError): solution.build_tree([1],[1,2])
    with pytest.raises(ValueError): solution.build_tree([1,2],[2,3])


def tree_diameter_of_tree():
    from python.tree.diameter_of_tree import DiameterOfBinaryTree
    solution=DiameterOfBinaryTree(); assert solution.diameter_of_binary_tree(tree())==4; assert solution.diameter_of_binary_tree(None)==0; assert solution.diameter_of_binary_tree(TreeNode(1))==0


def tree_good_nodes():
    from python.tree.good_nodes import GoodNodes
    solution=GoodNodes(); root=TreeNode(3,TreeNode(1,TreeNode(3)),TreeNode(4,TreeNode(1),TreeNode(5))); assert solution.good_nodes(root)==4; assert solution.good_nodes(None)==0


def tree_invert_tree():
    from python.tree.invert_tree import InvertTree
    solution=InvertTree(); root=tree(); assert solution.invert_tree(root) is root; assert root.left.val==6 and root.right.val==2; assert solution.invert_tree(None) is None


def tree_is_balanced():
    from python.tree.is_balanced import BalancedTree
    solution=BalancedTree(); assert solution.is_balanced(tree()); root=TreeNode(1,TreeNode(2,TreeNode(3))); assert not solution.is_balanced(root); assert solution.is_balanced_with_status(None)


def tree_is_same_tree():
    from python.tree.is_same_tree import SameTree
    solution=SameTree(); assert solution.is_same_tree(tree(),tree()); assert not solution.is_same_tree(TreeNode(1),TreeNode(2)); assert not solution.is_same_tree(TreeNode(1),None); assert solution.is_same_tree(None,None)


def tree_is_sub_tree():
    from python.tree.is_sub_tree import Subtree
    solution=Subtree(); root=tree(); assert solution.is_subtree(root,root.left); assert solution.is_subtree(root,None); assert not solution.is_subtree(None,TreeNode(1)); assert not solution.is_subtree(root,TreeNode(9))


def tree_kth_smallest_in_bst():
    from python.tree.kth_smallest_in_bst import KthSmallest
    solution=KthSmallest(); root=tree(); assert solution.kth_smallest(root,1)==1; assert solution.kth_smallest_iterative(root,7)==7
    with pytest.raises(ValueError): solution.kth_smallest(root,8)


def tree_lca_bst():
    from python.tree.lca_bst import LowestCommonAncestorBST
    solution=LowestCommonAncestorBST(); root=tree(); assert solution.lowest_common_ancestor(root,root.left.left,root.left.right) is root.left; assert solution.lowest_common_ancestor(root,root.left,root.right) is root; assert solution.lowest_common_ancestor_iterative(root,root.right.left,root.right.right) is root.right


def tree_least_common_ancestor():
    from python.tree.least_common_ancestor import LowestCommonAncestor
    solution=LowestCommonAncestor(); root=tree(); assert solution.lowest_common_ancestor(root,root.left.left,root.right.right) is root; assert solution.lowest_common_ancestor(root,root.left,root.left.right) is root.left; assert solution.lowest_common_ancestor(None,root.left,root.right) is None


def tree_max_depth():
    from python.tree.max_depth import MaxDepth
    solution=MaxDepth(); assert solution.max_depth(tree())==3; assert solution.max_depth(None)==0


def tree_max_path_sum():
    from python.tree.max_path_sum import MaxPathSum
    solution=MaxPathSum(); assert solution.max_path_sum(TreeNode(-10,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7))))==42; assert solution.max_path_sum(TreeNode(-3))==-3
    with pytest.raises(ValueError): solution.max_path_sum(None)


def tree_serializer():
    from python.tree.serializer import Codec
    from python.tree.is_same_tree import SameTree
    codec=Codec(); root=tree(); encoded=codec.serialize(root); assert SameTree().is_same_tree(codec.deserialize(encoded),root); assert codec.serialize(None)=="N" and codec.deserialize("N") is None
    with pytest.raises(ValueError): codec.deserialize("N,N")


def tree_tree_level_traversal():
    from python.tree.tree_level_traversal import LevelOrder
    solution=LevelOrder(); assert solution.level_order(tree())==[[4],[2,6],[1,3,5,7]]; assert solution.level_order(None)==[]


def tree_tree_node_distance():
    from python.tree.tree_node_distance import TreeNodeDistance
    solution=TreeNodeDistance(); assert solution.calculate_distance(tree(),1,7)==4; assert solution.calculate_distance(tree(),2,3)==1
    with pytest.raises(ValueError): solution.calculate_distance(tree(),1,99)
    with pytest.raises(ValueError): solution.calculate_distance(None,1,2)


def tree_valid_bst():
    from python.tree.valid_bst import ValidBST
    solution=ValidBST(); assert solution.is_valid_bst(tree()); assert not solution.is_valid_bst(TreeNode(5,TreeNode(1),TreeNode(4,TreeNode(3),TreeNode(6)))); assert solution.is_valid_bst(None)


def two_pointer_container_with_most_water():
    from python.two_pointer.container_with_most_water import ContainerWithMostWater
    solution=ContainerWithMostWater(); assert solution.max_area([1,8,6,2,5,4,8,3,7])==49; assert solution.max_area([])==0


def two_pointer_is_valid_palandrom():
    from python.two_pointer.is_valid_palandrom import ValidPalindrome
    solution=ValidPalindrome(); assert solution.is_palindrome("A man, a plan, a canal: Panama"); assert not solution.is_palindrome("race a car"); assert solution.is_palindrome_two_pointer(" "); assert not solution.is_palindrome_two_pointer("0P")


def two_pointer_length_of_longest_substring():
    from python.two_pointer.length_of_longest_substring import LongestSubstring
    solution=LongestSubstring()
    for value,expected in [("abcabcbb",3),("bbbbb",1),("",0),("dvdf",3)]: assert solution.length_of_longest_substring(value)==expected; assert solution.length_of_longest_substring_with_set(value)==expected


def two_pointer_longest_repeat_char_replacement():
    from python.two_pointer.longest_repeat_char_replacement import CharacterReplacement
    solution=CharacterReplacement(); assert solution.character_replacement("ABAB",2)==4; assert solution.character_replacement("AABABBA",1)==4; assert solution.character_replacement("",2)==0


def two_pointer_merge_intervals():
    from python.two_pointer.merge_intervals import MergeIntervals
    solution=MergeIntervals(); values=[[1,3],[2,6],[8,10],[15,18]]; assert solution.merge(values)==[[1,6],[8,10],[15,18]]; assert values==[[1,3],[2,6],[8,10],[15,18]]; assert solution.merge([])==[]


def two_pointer_reverse_only_letters():
    from python.two_pointer.reverse_only_letters import ReverseOnlyLetters
    solution=ReverseOnlyLetters(); assert solution.reverse_only_letters("a-bC-dEf-ghIj")=="j-Ih-gfE-dCba"; assert solution.reverse_only_letters("123")=="123"; assert solution.reverse_only_letters("")==""


def two_pointer_stock_trade():
    from python.two_pointer.stock_trade import StockTrade
    solution=StockTrade(); assert solution.max_profit([7,1,5,3,6,4])==5; assert solution.max_profit([7,6,4,3,1])==0; assert solution.max_profit([])==0


def two_pointer_string_permutation():
    from python.two_pointer.string_permutation import PermutationInString
    solution=PermutationInString(); assert solution.check_inclusion("ab","eidbaooo"); assert not solution.check_inclusion("ab","eidboaoo"); assert solution.check_inclusion("",""); assert not solution.check_inclusion("long","no")


def two_pointer_three_sum():
    from python.two_pointer.three_sum import ThreeSum
    solution=ThreeSum(); values=[-1,0,1,2,-1,-4]; assert {tuple(x) for x in solution.three_sum(values)}=={(-1,-1,2),(-1,0,1)}; assert values==[-1,0,1,2,-1,-4]; assert solution.three_sum([])==[]


def two_pointer_two_sum_input_sorted():
    from python.two_pointer.two_sum_input_sorted import TwoSumSorted
    solution=TwoSumSorted(); assert solution.two_sum([2,7,11,15],9)==[1,2]; assert solution.two_sum([1,2,3],9)==[]; assert solution.two_sum([],1)==[]


CASES = {name: value for name, value in globals().copy().items() if callable(value) and name.split("_", 1)[0] in {"array", "backtrack", "dynamic", "graph", "greedy", "heap", "interval", "linked", "search", "stack", "tree", "two"}}
