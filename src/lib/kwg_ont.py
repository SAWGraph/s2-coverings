from rdflib import DC, DCTERMS, OWL, PROV, RDF, RDFS, SDO, SKOS, XMLNS, XSD, URIRef
from rdflib.namespace import DefinedNamespace, Namespace
from s2geometry import S2Cell, S2CellId


class KWGOnt(DefinedNamespace):
    kwg_endpoint = "http://stko-kwg.geog.ucsb.edu/"

    KWGR = Namespace(f"{kwg_endpoint}lod/resource/")

    S2Cell_Level0: URIRef
    S2Cell_Level1: URIRef
    S2Cell_Level2: URIRef
    S2Cell_Level3: URIRef
    S2Cell_Level4: URIRef
    S2Cell_Level5: URIRef
    S2Cell_Level6: URIRef
    S2Cell_Level7: URIRef
    S2Cell_Level8: URIRef
    S2Cell_Level9: URIRef
    S2Cell_Level10: URIRef
    S2Cell_Level11: URIRef
    S2Cell_Level12: URIRef
    S2Cell_Level13: URIRef

    cellID: URIRef

    sfEquals: URIRef
    sfContains: URIRef
    sfWithin: URIRef
    sfTouches: URIRef
    sfOverlaps: URIRef
    sfCrosses: URIRef
    vertexPolygon: URIRef

    _NS = Namespace(f"{kwg_endpoint}lod/ontology/")
    
    
class SPATIAL(DefinedNamespace):
    SPATIAL_ENDPOINT = "http://purl.org/"
    
    connectedTo: URIRef
    
    _NS = Namespace(f'{SPATIAL_ENDPOINT}spatialai/spatial/spatial-full#')


def generate_cell_iri(cell_id: S2CellId) -> URIRef:
    """
    Creates an IRI for an individual cell, with a KnowWhereGraph domain

    Args:
        cell_id: The ID of the s2 cell
    Returns:
         A URI of the s2 cell
    """
    level = cell_id.level()
    id_str = cell_id.id()
    return KWGOnt.KWGR[f"{'s2.level'}{level}.{id_str}"]


# namespace_prefix = {
    # "kwgr": KWGOnt.KWGR,
    # "kwg-ont": KWGOnt._NS,
    # "geo": Namespace("http://www.opengis.net/ont/geosparql#"),
    # "sf": Namespace("http://www.opengis.net/ont/sf#"),
    # "rdf": RDF,
    # "rdfs": RDFS,
    # "xsd": XSD,
# }

namespace_prefix = {
    "co_cgs": Namespace(f'http://sawgraph.spatialai.org/v1/co-cgs#'),
    "co_cgs_data": Namespace(f'http://sawgraph.spatialai.org/v1/co-cgs-data#'),
    "coso": Namespace(f'http://w3id.org/coso/v1/contaminoso#'),
    "dc": DC,
    "dcgeoid": Namespace(f'https://datacommons.org/browser/geoId/'),
    "dcterms": DCTERMS,  # or "terms" ?
    "epa_frs": Namespace(f'http://w3id.org/fio/v1/epa-frs#'),
    "epa_frs_data": Namespace(f'http://w3id.org/fio/v1/epa-frs-data#'),
    "fio-pfas": Namespace(f'http://w3id.org/fio/v1/pfas#'),
    "fio": Namespace(f'http://w3id.org/fio/v1/fio#'),
    "gcx": Namespace(f'https://geoconnex.us/'),
    "gcx_cid": Namespace(f'https://geoconnex.us/nhdplusv2/comid/'),
    "gcx_ms": Namespace(f'https://geoconnex.us/ref/mainstems/'),
    "gsmlb": Namespace(f'http://geosciml.org/def/gsmlb#'),
    "gwml2": Namespace(f'http://gwml2.org/def/gwml2#'),
    "hyf": Namespace(f'https://www.opengis.net/def/schema/hy_features/hyf/'),
    "hyfo": Namespace(f'http://hyfo.spatialai.org/v1/hyfo#'),
    "il_isgs": Namespace(f'http://sawgraph.spatialai.org/v1/il-isgs#'),
    "il_isgs_data": Namespace(f'http://sawgraph.spatialai.org/v1/il-isgs-data#'),
    "kwg-ont": Namespace(f'http://stko-kwg.geog.ucsb.edu/lod/ontology/'),
    "kwgr": Namespace(f'http://stko-kwg.geog.ucsb.edu/lod/resource/'),
    "me_egad": Namespace(f'http://w3id.org/sawgraph/v1/me-egad#'),
    "me_egad_data": Namespace(f'http://w3id.org/sawgraph/v1/me-egad-data#'),
    "me_mgs": Namespace(f'http://sawgraph.spatialai.org/v1/me-mgs#'),
    "me_mgs_data": Namespace(f'http://sawgraph.spatialai.org/v1/me-mgs-data#'),
    "naics": Namespace(f'http://w3id.org/fio/v1/naics#'),
    "nhdplusv2": Namespace(f'http://nhdplusv2.spatialai.org/v1/nhdplusv2#'),
    "obo": Namespace(f'http://purl.obolibrary.org/obo/'),
    "owl": OWL,
    "pfas": Namespace(f'http://sawgraph.spatialai.org/v1/pfas#'),
    "prov": PROV,
    "quantitykind": Namespace(f'http://qudt.org/vocab/quantitykind/'),
    "qudt": Namespace(f'http://qudt.org/schema/qudt/'),
    "rdf": RDF,
    "rdfs": RDFS,
    "saw_geo": Namespace(f'http://sawgraph.spatialai.org/v1/saw_geo#'),
    "schema": SDO,
    "sf": Namespace(f'http://www.opengis.net/ont/sf#'),
    "skos": SKOS,
    "sosa": Namespace('http://www.w3.org/ns/sosa/'),
    "spatial": Namespace(f'http://purl.org/spatialai/spatial/spatial-full#'),
    "stad": Namespace(f'http://purl.org/spatialai/stad/v2/core/'),
    "time": Namespace(f'http://www.w3.org/2006/time#'),
    "unit": Namespace(f'http://qudt.org/vocab/unit/'),
    "us_sdwis": Namespace(f'http://sawgraph.spatialai.org/v1/us-sdwis#'),
    "usgs": Namespace(f'http://usgs.spatialai.org/v1/usgs#'),
    "usgs_data": Namespace(f'http://usgs.spatialai.org/v1/usgs-data#'),
    "usgwd": Namespace(f'http://w3id.org/hyfo/usgwd/v1/usgwd#'),
    "wbd": Namespace(f'http://wbd.spatialai.org/v1/wbd#'),
    "wbd_data": Namespace(f'http://wbd.spatialai.org/v1/wbd-data#'),
    "wdt": Namespace(f'https://www.wikidata.org/prop/direct/'),
    "xml": XMLNS,
    "xsd": XSD
}

