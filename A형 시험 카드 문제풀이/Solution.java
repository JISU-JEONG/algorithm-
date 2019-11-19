package Shuffle_O_Matic;

import java.util.Scanner;

public class Solution {
	static int N;
	static int card[];
	static int[] card_down;
	static int ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			ans = -1;
			card = new int[N];
			for (int i = 0; i < N; i++) {
				card[i] = sc.nextInt();
			}
			up(card, 0);
			if(ans>1)
				ans--;
			System.out.println("#" + tc + " " + ans);
		}
	}

	static void up(int[] card_up, int cnt) {
		for (int i = 0; i < N; i++) {
			if (card_up[i] != i + 1)
				break;
			else if (i == N - 1) {
				if (ans == -1 || cnt < ans) {
					ans = cnt;
				}
			}
		}
		for (int i = 0; i < N; i++) {
			if (card_up[i] != N - i)
				break;
			else if (i == N - 1) {
				if (ans == -1 || cnt < ans) {
					ans = cnt;
				}
			}
		}
		cnt++;
		if (cnt == 7)
			return;
		for (int i = 1; i < N; i++) {
			up(make_card(card_up, i), cnt);
		}
	}

	private static int[] make_card(int[] card_up, int i) {
		int[] temp_card = new int[N];
		for (int j = 0; j < N; j++) {
			temp_card[j] = 0;
		}
		if (i <= N / 2) {
			int pos = 0;
			for (int j = 0; j < N / 2; j++) {
				if (j + i < N / 2) {
					temp_card[pos++] = card_up[j];
				} else {
					temp_card[++pos] = card_up[j];
					pos++;
				}
			}
			for (int j = N / 2; j < N; j++) {
				for (int j2 = 0; j2 < N; j2++) {
					if (temp_card[j2] == 0) {
						temp_card[j2] = card_up[j];
						break;
					}
				}
			}
		} else {
			int pos = 0;
			for (int j = N / 2; j < N; j++) {
				if (j < i + 1) {
					temp_card[pos++] = card_up[j];
				} else {
					temp_card[++pos] = card_up[j];
					pos = pos++;
				}
			}
			for (int j = 0; j < N / 2; j++) {
				for (int j2 = 0; j2 < N; j2++) {
					if (temp_card[j2] == 0) {
						temp_card[j2] = card_up[j];
						break;
					}
				}
			}
		}
		return temp_card;
	}
}
