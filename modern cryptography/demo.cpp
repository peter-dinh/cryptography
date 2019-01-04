/* Do the A5/1 key setup.  This routine accepts a 64-bit key and a 22-bit frame number. */
void keysetup(byte key[8], word frame) {
	int i;
	bit keybit, framebit;

	/* Zero out the shift registers. */
	R1 = R2 = R3 = 0;

	/* Load the key into the shift registers,
	 * LSB of first byte of key array first,
	 * clocking each register once for every
	 * key bit loaded.  (The usual clock
	 * control rule is temporarily disabled.) */
	for (i=0; i<64; i++) {
		clockallthree(); /* always clock */
		keybit = (key[i/8] >> (i&7)) & 1; /* The i-th bit of the key */
		R1 ^= keybit; R2 ^= keybit; R3 ^= keybit;
	}

	/* Load the frame number into the shift
	 * registers, LSB first,
	 * clocking each register once for every
	 * key bit loaded.  (The usual clock
	 * control rule is still disabled.) */
	for (i=0; i<22; i++) {
		clockallthree(); /* always clock */
		framebit = (frame >> i) & 1; /* The i-th bit of the frame # */
		R1 ^= framebit; R2 ^= framebit; R3 ^= framebit;
	}

	/* Run the shift registers for 100 clocks
	 * to mix the keying material and frame number
	 * together with output generation disabled,
	 * so that there is sufficient avalanche.
	 * We re-enable the majority-based clock control
	 * rule from now on. */
	for (i=0; i<100; i++) {
		clock();
	}

}

int main(){
    
}