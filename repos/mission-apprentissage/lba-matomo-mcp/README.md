# lba-matomo-mcp

Serveur MCP (Streamable HTTP, Vercel) qui pilote le conteneur Matomo Tag Manager de La bonne alternance (`s4n03ZE1`, site 7 sur `stats.beta.gouv.fr`) via l'API HTTP `TagManager.*`, et lit les statistiques agrégées du site via l'API de reporting.

Les écritures visent uniquement le **brouillon** du conteneur. Rien n'atteint les internautes avant `create_version` puis `publish_version` sur `live`.

## Variables d'environnement

| Variable | Défaut | Rôle |
| --- | --- | --- |
| `MCP_SECRET` | aucun, **obligatoire** | Secret de **lecture seule**, attendu en `Authorization: Bearer <secret>` (ou `Basic <secret>`, ou `?token=`). Sans lui, toutes les requêtes reçoivent une 503. |
| `MCP_WRITE_SECRET` | aucun | Secret d'**écriture et de publication**, réservé aux devs. Absent : personne n'écrit. Identique à `MCP_SECRET` : 503. |
| `MATOMO_TOKEN` | aucun, obligatoire | Jeton Matomo « sécurisé uniquement », envoyé en `Authorization: Bearer`. Il a **tous les droits du compte** qui l'a créé, sur tous les sites. |
| `MATOMO_URL` | `https://stats.beta.gouv.fr` | |
| `MATOMO_ID_SITE` | `7` | |
| `MATOMO_ID_CONTAINER` | `s4n03ZE1` | |

## Accès

L'URL est la même pour tout le monde, c'est le secret présenté qui fixe l'accès :

| Secret | Pour qui | Outils |
| --- | --- | --- |
| `MCP_SECRET` | tout le monde | lecture ; `track_custom_event` simule seulement |
| `MCP_WRITE_SECRET` | devs | lecture, écriture sur le brouillon, publication |

Pour couper l'écriture : supprimer ou changer `MCP_WRITE_SECRET` sur Vercel, puis redéployer. Les deux secrets passent par le même `MATOMO_TOKEN` : l'accès lecture limite ce que l'agent peut faire, pas les droits du jeton.

## Outils

- Lecture : `get_container`, `list_versions`, `get_version`, `list_triggers`, `get_trigger`, `list_tags`, `get_tag`, `list_variables`, `get_variable`, `get_references`, `find_orphan_triggers`, `export_version`, `list_reference_data`.
- Statistiques (agrégats, lecture) : `list_reports`, `list_goals_and_dimensions`, `get_report` (liste blanche de rapports : trafic, pages, événements, acquisition, objectifs, dimensions, audience, entonnoirs, formulaires, heatmaps, parcours, cohortes, transitions, performance, rapports personnalisés ; ni `Live` ni enregistrements de session), `check_tag_activity` (balises de la version live croisées avec les événements reçus), `list_analytics_setup`, `test_funnel_steps`, `test_heatmap_page_rules`, `list_annotations`.
- Haut niveau : `track_custom_event` (déclencheur `dl__<event>` + balise `<catégorie>__<action>`, `dry_run` pour voir le plan).
- Écriture, avec `MCP_WRITE_SECRET` : `add_|update_|delete_` + `trigger|tag|variable`, `pause_tag`, `resume_tag`, `create_version`, `publish_version` (`dev` par défaut, `live` exige `confirm_live=true` et ajoute une annotation Matomo), `save_funnel`, `save_heatmap`, `set_heatmap_status`, `save_custom_report`, `add_annotation`.
