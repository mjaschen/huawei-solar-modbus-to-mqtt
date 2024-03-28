# Huawei Solar Inverter Modbus 2 MQTT

## Installation

### venv

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Create config file
cp .env.template .env
vi .env
```

Run the script:

```shell
./run.sh
```

### Docker

```shell
cp .env.template .env.docker
vi .env.docker
docker build -t huawei-solar-modbus-to-mqtt:latest .
docker run --rm -it huawei-solar-modbus-to-mqtt:latest
```

## Result from querying primary inverter

```
{'accumulated_yield_energy': Result(value=77.92, unit='kWh'),
 'active_grid_A_B_voltage': Result(value=406.8, unit='V'),
 'active_grid_A_current': Result(value=-2.07, unit='I'),
 'active_grid_A_power': Result(value=-173, unit='W'),
 'active_grid_B_C_voltage': Result(value=407.8, unit='V'),
 'active_grid_B_current': Result(value=-0.35, unit='I'),
 'active_grid_B_power': Result(value=-47, unit='W'),
 'active_grid_C_A_voltage': Result(value=407.2, unit='V'),
 'active_grid_C_current': Result(value=-0.64, unit='I'),
 'active_grid_C_power': Result(value=-92, unit='W'),
 'active_grid_frequency': Result(value=50.0, unit='Hz'),
 'active_grid_power_factor': Result(value=-0.432, unit=None),
 'active_power': Result(value=-17, unit='W'),
 'alarm_1': Result(value=[], unit=None),
 'alarm_2': Result(value=[], unit=None),
 'alarm_3': Result(value=[], unit=None),
 'daily_yield_energy': Result(value=0.0, unit='kWh'),
 'day_active_power_peak': Result(value=12, unit='W'),
 'device_status': Result(value='On-grid', unit=None),
 'efficiency': Result(value=100.0, unit='%'),
 'fault_code': Result(value=0, unit=None),
 'grid_A_voltage': Result(value=234.6, unit='V'),
 'grid_B_voltage': Result(value=235.3, unit='V'),
 'grid_C_voltage': Result(value=235.8, unit='V'),
 'grid_accumulated_energy': Result(value=182.78, unit='kWh'),
 'grid_accumulated_reactive_power': Result(value=0.0, unit='kVarh'),
 'grid_exported_energy': Result(value=4.05, unit='kWh'),
 'grid_frequency': Result(value=50.01, unit='Hz'),
 'input_power': Result(value=-17, unit='W'),
 'insulation_resistance': Result(value=30.0, unit='MOhm'),
 'internal_temperature': Result(value=33.4, unit='°C'),
 'line_voltage_A_B': Result(value=235.4, unit='V'),
 'line_voltage_B_C': Result(value=0.0, unit='V'),
 'line_voltage_C_A': Result(value=0.0, unit='V'),
 'meter_status': Result(value=<MeterStatus.NORMAL: 1>, unit=None),
 'meter_type': Result(value=<MeterType.THREE_PHASE: 1>, unit=None),
 'phase_A_current': Result(value=0.287, unit='A'),
 'phase_A_voltage': Result(value=116.2, unit='V'),
 'phase_B_current': Result(value=0.0, unit='A'),
 'phase_B_voltage': Result(value=0.1, unit='V'),
 'phase_C_current': Result(value=0.0, unit='A'),
 'phase_C_voltage': Result(value=0.0, unit='V'),
 'power_factor': Result(value=0.997, unit=None),
 'power_meter_active_power': Result(value=-313, unit='W'),
 'power_meter_reactive_power': Result(value=598, unit='Var'),
 'pv_01_current': Result(value=0.0, unit='A'),
 'pv_01_voltage': Result(value=157.6, unit='V'),
 'pv_02_current': Result(value=0.0, unit='A'),
 'pv_02_voltage': Result(value=130.6, unit='V'),
 'reactive_power': Result(value=1, unit='VA'),
 'shutdown_time': Result(value=None, unit=None),
 'startup_time': Result(value=datetime.datetime(2023, 11, 18, 7, 51, 5, tzinfo=datetime.timezone.utc), unit=None),
 'state_1': Result(value=['Grid-Connected',
Grid-Connected normally'], unit=None),
 'state_2': Result(value=['Unlocked',
PV connected',
DSP data collection'], unit=None),
 'state_3': Result(value=['On-grid',
Off-grid switch disabled'], unit=None),
 'storage_bus_current': Result(value=0.0, unit='A'),
 'storage_bus_voltage': Result(value=434.8, unit='V'),
 'storage_charge_discharge_power': Result(value=0, unit='W'),
 'storage_current_day_charge_capacity': Result(value=0.21, unit='kWh'),
 'storage_current_day_discharge_capacity': Result(value=0.0, unit='kWh'),
 'storage_running_status': Result(value=<StorageStatus.RUNNING: 2>, unit=None),
 'storage_state_of_capacity': Result(value=7.0, unit='%'),
 'storage_total_charge': Result(value=62.38, unit='kWh'),
 'storage_total_discharge': Result(value=62.66, unit='kWh')}
```

## Result from Querying Configuration Registers

```
{'storage_maximum_charging_power': Result(value=2500, unit='W'),
storage_maximum_discharging_power': Result(value=2500, unit='W'),
storage_charging_cutoff_capacity': Result(value=100.0, unit='%'),
storage_discharging_cutoff_capacity': Result(value=7.0, unit='%'),
storage_working_mode_settings': Result(value=<StorageWorkingModesC.MAXIMISE_SELF_CONSUMPTION: 2>, unit=None),
storage_charge_from_grid_function': Result(value=True, unit=None),
storage_grid_charge_cutoff_state_of_charge': Result(value=50.0, unit='%'),
storage_fixed_charging_and_discharging_periods': Result(value=[], unit=None),
storage_power_of_charge_from_grid': Result(value=3000, unit='W'),
storage_maximum_power_of_charge_from_grid': Result(value=3000, unit='W'),
storage_time_of_use_charging_and_discharging_periods': Result(value=[HUAWEI_LUNA2000_TimeOfUsePeriod(start_time=0, end_time=360, charge_flag=<ChargeFlag.CHARGE: 0>, days_effective=(True, True, True, True, True, True, True)), HUAWEI_LUNA2000_TimeOfUsePeriod(start_time=480, end_time=1320, charge_flag=<ChargeFlag.DISCHARGE: 1>, days_effective=(True, True, True, True, True, True, True))], unit=None),
storage_excess_pv_energy_use_in_tou': Result(value=<StorageExcessPvEnergyUseInTOU.FED_TO_GRID: 0>, unit=None),
storage_backup_power_state_of_charge': Result(value=0.0, unit='%'),
storage_capacity_control_mode': Result(value=<StorageCapacityControlMode.DISABLE: 0>, unit=None),
storage_capacity_control_soc_peak_shaving': Result(value=50.0, unit='%'),
storage_capacity_control_periods': Result(value=[], unit=None)}
```
