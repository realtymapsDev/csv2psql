# from PostgreSQL 8.4 documentation
psql_reserved_words = ["a", "abs", "absent", "according", "ada", "all", "allocate", "alter",
 "analyse", "analyze", "and", "any", "are", "array", "array_agg", "as", "asc",
 "asensitive", "asymmetric", "at", "atomic", "attribute", "attributes",
 "authorization", "avg", "base64", "begin", "bernoulli", "between", "bigint",
 "binary", "blob", "bom", "boolean", "both", "breadth", "by", "c", "call",
 "called", "cardinality", "cascaded", "case", "cast", "catalog_name", "ceil",
 "ceiling", "char", "character", "characters", "character_length",
 "character_set_catalog", "character_set_name", "character_set_schema",
 "char_length", "check", "class_origin", "clob", "close", "coalesce", "cobol",
 "collate", "collation", "collation_catalog", "collation_name",
 "collation_schema", "collect", "column", "columns", "column_name",
 "command_function", "command_function_code", "commit", "condition",
 "condition_number", "connect", "connection_name", "constraint",
 "constraint_catalog", "constraint_name", "constraint_schema", "constructor",
 "contains", "convert", "corr", "corresponding", "count", "covar_pop",
 "covar_samp", "create", "cross", "cube", "cume_dist", "current",
 "current_catalog", "current_date", "current_default_transform_group",
 "current_path", "current_role", "current_schema", "current_time",
 "current_timestamp", "current_transform_group_for_type", "current_user",
 "cursor", "cursor_name", "cycle", "date", "datetime_interval_code",
 "datetime_interval_precision", "day", "deallocate", "dec", "decimal",
 "declare", "default", "deferrable", "defined", "degree", "delete",
 "dense_rank", "depth", "deref", "derived", "desc", "describe", "descriptor",
 "deterministic", "diagnostics", "disconnect", "dispatch", "distinct", "do",
 "double", "drop", "dynamic", "dynamic_function", "dynamic_function_code",
 "each", "element", "else", "empty", "end", "end-exec", "equals", "escape",
 "every", "except", "exclude", "exec", "execute", "exists", "exp", "external",
 "extract", "false", "fetch", "filter", "final", "first_value", "flag",
 "float", "floor", "following", "for", "foreign", "fortran", "found", "free",
 "freeze", "from", "full", "function", "fusion", "g", "general", "generated",
 "get", "global", "go", "goto", "grant", "group", "grouping", "having", "hex",
 "hierarchy", "hold", "hour", "id", "identity", "ignore", "ilike",
 "implementation", "in", "indent", "indicator", "initially", "inner", "inout",
 "insensitive", "insert", "instance", "instantiable", "int", "integer",
 "intersect", "intersection", "interval", "into", "is", "isnull", "join", "k",
 "key_member", "key_type", "lag", "language", "large", "last_value", "lateral",
 "lead", "leading", "left", "length", "like", "like_regex", "limit", "ln",
 "local", "localtime", "localtimestamp", "locator", "lower", "m", "map",
 "match", "matched", "max", "max_cardinality", "member", "merge",
 "message_length", "message_octet_length", "message_text", "method", "min",
 "minute", "mod", "modifies", "module", "month", "more", "multiset", "mumps",
 "namespace", "national", "natural", "nchar", "nclob", "nesting", "new", "nfc",
 "nfd", "nfkc", "nfkd", "nil", "no", "none", "normalize", "normalized", "not",
 "notnull", "nth_value", "ntile", "null", "nullable", "nullif", "number",
 "numeric", "occurrences_regex", "octets", "octet_length", "of", "off",
 "offset", "old", "on", "only", "open", "or", "order", "ordering",
 "ordinality", "others", "out", "outer", "output", "over", "overlaps",
 "overlay", "overriding", "p", "pad", "parameter", "parameter_mode",
 "parameter_name", "parameter_ordinal_position", "parameter_specific_catalog",
 "parameter_specific_name", "parameter_specific_schema", "partition", "pascal",
 "passing", "path", "percentile_cont", "percentile_disc", "percent_rank",
 "placing", "pli", "position", "position_regex", "power", "preceding",
 "precision", "prepare", "primary", "procedure", "public", "range", "rank",
 "reads", "real", "recursive", "ref", "references", "referencing", "regr_avgx",
 "regr_avgy", "regr_count", "regr_intercept", "regr_r2", "regr_slope",
 "regr_sxx", "regr_sxy", "regr_syy", "release", "respect", "result", "return",
 "returned_cardinality", "returned_length", "returned_octet_length",
 "returned_sqlstate", "returning", "returns", "revoke", "right", "rollback",
 "rollup", "routine", "routine_catalog", "routine_name", "routine_schema",
 "row", "rows", "row_count", "row_number", "savepoint", "scale", "schema_name",
 "scope", "scope_catalog", "scope_name", "scope_schema", "scroll", "search",
 "second", "section", "select", "self", "sensitive", "server_name",
 "session_user", "set", "sets", "similar", "size", "smallint", "some",
 "source", "space", "specific", "specifictype", "specific_name", "sql",
 "sqlexception", "sqlstate", "sqlwarning", "sqrt", "start", "state", "static",
 "stddev_pop", "stddev_samp", "structure", "style", "subclass_origin",
 "submultiset", "substring", "substring_regex", "sum", "symmetric", "system",
 "system_user", "t", "table", "tablesample", "table_name", "then", "ties",
 "time", "timestamp", "timezone_hour", "timezone_minute", "to",
 "top_level_count", "trailing", "transactions_committed",
 "transactions_rolled_back", "transaction_active", "transform", "transforms",
 "translate", "translate_regex", "translation", "treat", "trigger",
 "trigger_catalog", "trigger_name", "trigger_schema", "trim", "trim_array",
 "true", "truncate", "uescape", "unbounded", "under", "union", "unique",
 "unknown", "unnamed", "unnest", "untyped", "update", "upper", "uri", "usage",
 "user", "user_defined_type_catalog", "user_defined_type_code",
 "user_defined_type_name", "user_defined_type_schema", "using", "value",
 "values", "varbinary", "varchar", "variadic", "varying", "var_pop",
 "var_samp", "verbose", "when", "whenever", "where", "width_bucket", "window",
 "with", "within", "without", "xml", "xmlagg", "xmlattributes", "xmlbinary",
 "xmlcast", "xmlcomment", "xmlconcat", "xmldeclaration", "xmldocument",
 "xmlelement", "xmlexists", "xmlforest", "xmliterate", "xmlnamespaces",
 "xmlparse", "xmlpi", "xmlquery", "xmlschema", "xmlserialize", "xmltable",
 "xmltext", "xmlvalidate", "year"]
