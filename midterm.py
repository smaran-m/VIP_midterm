# import lines
from sparc.sparc_core import SPARC
from ase.build import molecule
from ase.units import kJ, mol

water = molecule('H2O')
hydrogen = molecule('H2')
oxygen = molecule('O2')
water.cell = [[6,0,0],[0,6,0],[0,0,6]]
water.center()
hydrogen.cell = [[6,0,0],[0,6,0],[0,0,6]]
hydrogen.center()
water.cell = [[6,0,0],[0,6,0],[0,0,6]]
oxygen.center()
water_energy = []
hydrogen_energy = []
oxygen_energy = []
reaction_energy = []
error = []

# set up the calculator
grid_spacings = [0.2, 0.16, 0.14, 0.12]
for i in grid_spacings:
        calc = SPARC(
                KPOINT_GRID=[1,1,1],
                h = i,
                EXCHANGE_CORRELATION = 'GGA_PBE',
                TOL_SCF=1e-5,
                RELAX_FLAG=1,
                PRINT_FORCES=1,
                PRINT_RELAXOUT=1)

        water.set_calculator(calc)
        hydrogen.set_calculator(calc)
        oxygen.set_calculator(calc)

        Ew = water.get_potential_energy()
        Eh = hydrogen.get_potential_energy()
        Eo = oxygen.get_potential_energy()
        water_energy.append(Ew)
        hydrogen_energy.append(Eh)
        oxygen_energy.append(Eo)

        renergy = (Eh + 0.5 * Eo - Ew)
        reaction_energy.append(renergy)
        error.append(100 * ((renergy - (285.8261 * kJ / mol)) / (285.8261 * kJ / mol)))

# set the calculator on the atoms and run
for i in reaction_energy:
        print("Grid spacing:", grid_spacings[reaction_energy.index(i)])
        print("Reaction energy of\nH2O: {:4f} eV\nH2: {:4f} eV\nO2: {:4f} eV".format(water_energy[reaction_energy.index(i)], hydrogen_energy[reaction_energy.index(i)], oxygen_energy[reaction_energy.index(i)]))
        print("1 mol of h2o: {:4f} eV".format(i))
        print("2 mol of h2o: {:4f} eV".format(2*i))
        print("error percentage: {:2f}%".format(error[reaction_energy.index(i)]))
