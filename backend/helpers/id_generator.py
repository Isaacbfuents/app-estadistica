def create_generator_id():
    next_id = 1

    def generate_id():
        nonlocal next_id
        current_id = next_id
        next_id += 1
        return current_id

    return generate_id

generate_type_id = create_generator_id()
