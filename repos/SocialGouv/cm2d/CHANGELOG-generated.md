## Changelog : cm2d (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la visualisation des données, notamment l'ajout de la cartographie des données pour les Départements et Régions d'Outre-Mer (DROM) et une meilleure gestion de la granularité des données sur les courbes. L'application est également plus flexible avec l'ajout d'une option "France entière" et une option "France hexagonale".

### Évolutions fonctionnelles
- Ajout de la cartographie des DROM via `react-simple-maps` et des fichiers GeoJSON [#29d2419](https://github.com/SocialGouv/cm2d/commit/29d2419).
- Possibilité de sélectionner la granularité des données sur les courbes (semaine, jour, mois) [#0837964](https://github.com/SocialGouv/cm2d/commit/0837964).
- Ajout d'une option "France entière" pour le rôle `region-france-entiere` [#be3f9dc](https://github.com/SocialGouv/cm2d/commit/be3f9dc).
- Ajout d'une option "France hexagonale" (métropole hors DROM) [#57105de](https://github.com/SocialGouv/cm2d/commit/57105de).
- Amélioration du centrage et du recadrage de la carte sur la région sélectionnée [#4bfe1a4](https://github.com/SocialGouv/cm2d/commit/4bfe1a4).
- Infobulles au survol des régions sur la carte, avec une colorimétrie basée sur la médiane et un seed pondéré [#2548caf](https://github.com/SocialGouv/cm2d/commit/2548caf).
- Amélioration du centrage vertical des encarts DROM face à la carte [#83b7977](https://github.com/SocialGouv/cm2d/commit/83b7977).
- Correction de l'affichage de la comparaison par année sur un axe commun (mois/semaine/jour) [#e46a1ef](https://github.com/SocialGouv/cm2d/commit/e46a1ef).
- Affichage de toutes les régions disponibles [#9d65629](https://github.com/SocialGouv/cm2d/commit/9d65629).

### Évolutions techniques
- Mise à jour de la version d'Elasticsearch à 8.9.0 et de Yarn à la version 4 corepack dans le Dockerfile pour assurer la compatibilité avec Node 18 [#fb272ab](https://github.com/SocialGouv/cm2d/commit/fb272ab).
- Scripts idempotents pour l'initialisation et le seed d'Elasticsearch [#634b8ca](https://github.com/SocialGouv/cm2d/commit/634b8ca).
- Correction de la stratification par région pour les versions d'Elasticsearch inférieures à 7.11 [#daf5135](https://github.com/SocialGouv/cm2d/commit/daf5135).
- Ajout des DROM à la liste des départements et régions [#fae53d7](https://github.com/SocialGouv/cm2d/commit/fae53d7).
- Stratification par région étendue à la France entière [#102e64d](https://github.com/SocialGouv/cm2d/commit/102e64d).

### Autres changements
- Ajout d'un nouveau favicon au format ICO et PNG [#a143e93](https://github.com/SocialGouv/cm2d/commit/a143e93).
