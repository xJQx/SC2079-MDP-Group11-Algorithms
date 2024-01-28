package main;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

public class MainApp {static double shortest = 1000000;
	private static Deque<Integer> route = new ArrayDeque<>();
	private static List<Integer> solution;
	
	
	static double graph1[][] = {
				{0,20,42,25},
				{20,0,30,34},
				{42,30,0,10},
				{25,34,10,0}
		};//test data
	public static void main(String[] args) {
		System.out.println("Hello World!");
		System.out.println(Arrays.toString(greedyHeuristic(graph1, 4)));
		System.out.println(Arrays.toString(exhaustive(graph1, 4)));
	}
	
	public static int[] greedyHeuristic(double graph[][], int n) {
		int[] path = new int[n];
		boolean[] visited = new boolean[n];
		int curr = 0;
		int nextNode= -1;
		for(int i = 0; i<n; i++) {
			visited[curr] = true;
			double min = 100000;
			for(int k = 0; k<n; k ++)
			{
				if(visited[k] != true) {
					if(graph[curr][k]< min) {
						min = graph[curr][k];
						nextNode = k;
					}
				}
			}
			visited[0] = true;
			path[i] = curr;
			curr = nextNode;
		}
		
		return path;
	}
	public static int[] exhaustive(double graph[][], int n) {

		int[] path = new int[n];
		boolean[] visited = new boolean[n];
		for(int i = 0; i<4; i++) {
			visited[i] = false;
		}
		step(visited, 0, 0, n);
		for(int i = 0; i<n; i++) {
			path[i] = solution.remove(n-i-1);
		}
		return path;
	}
	
	public static void step(boolean[] wentTo, int currentCity, double distance, int n)
    {
        int wentToCount = 0;
        for (int i = 0; i < n; ++i)
        {
            if (wentTo[i])
            {
                ++wentToCount;
                continue;
            }
            boolean[] copy = new boolean[n];
            System.arraycopy(wentTo, 0, copy, 0, n);
            copy[i] = true;
            double dist = distance + graph1[currentCity][i];
            route.push(i);
            step(copy, i, dist, n);
            int j = route.pop();
            assert j == i : "Got wrong town off stack, " + j + " instead of " + i;
        }
        if (wentToCount == 4)
        {
        	distance = distance + graph1[currentCity][0];
            if (shortest > distance)
            {
                shortest = distance;
                solution = new ArrayList<>(route);
            }
        }
    }
}
