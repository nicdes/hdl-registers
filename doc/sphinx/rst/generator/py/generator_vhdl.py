# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the hdl_registers project, a HDL register generator fast enough to run
# in real time.
# https://hdl-registers.com
# https://gitlab.com/hdl_registers/hdl_registers
# --------------------------------------------------------------------------------------------------

# Standard libraries
import sys
from pathlib import Path

# First party libraries
from hdl_registers.generator.vhdl.axi_lite_wrapper import VhdlAxiLiteWrapperGenerator
from hdl_registers.generator.vhdl.record_package import VhdlRecordPackageGenerator
from hdl_registers.generator.vhdl.register_package import VhdlRegisterPackageGenerator
from hdl_registers.generator.vhdl.simulation_package import VhdlSimulationPackageGenerator
from hdl_registers.parser.toml import from_toml

THIS_DIR = Path(__file__).parent


def main(output_folder: Path):
    """
    Create register VHDL artifacts from the "counter" example module.
    """
    register_list = from_toml(
        name="counter", toml_file=THIS_DIR.parent / "sim" / "regs_counter.toml"
    )

    VhdlRegisterPackageGenerator(
        register_list=register_list, output_folder=output_folder
    ).create_if_needed()

    VhdlRecordPackageGenerator(
        register_list=register_list, output_folder=output_folder
    ).create_if_needed()

    VhdlSimulationPackageGenerator(
        register_list=register_list, output_folder=output_folder
    ).create_if_needed()

    VhdlAxiLiteWrapperGenerator(
        register_list=register_list, output_folder=output_folder
    ).create_if_needed()


if __name__ == "__main__":
    main(output_folder=Path(sys.argv[1]))
