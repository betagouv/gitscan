# Synthèse d'activité : betagouv (du 01/04 au 15/11)

## Résumé de l'activité
L'activité de l'organisation est marquée par des transformations structurelles majeures, notamment l'intégration de l'intelligence artificielle pour l'analyse de données dans [portail-rse](/repos/betagouv/portail-rse) et [portail-rse-externe](/repos/betagouv/portail-rse-externe). Plusieurs projets clés ont entamé des refontes architecturales profondes pour gagner en modularité, à l'image de [transport-sanitaire](/repos/betagouv/transport-sanitaire) qui sépare désormais son moteur de simulation de ses règles métier, ou de [turgot-fiches-collectivites](/repos/betagouv/turgot-fiches-collectivites) qui change d'identité pour devenir "Fico".

Parallèlement, un effort important est déployé sur l'amélioration de l'expérience utilisateur via la cartographie interactive ([pnm](/repos/betagouv/pnm), [nitrates](/repos/betagouv/nitrates), [patrinotes](/repos/betagouv/patrinotes)) et l'accessibilité numérique ([sante-mentale-etudiant](/repos/betagouv/sante-mentale-etudiant), [sites-faciles](/repos/betagouv/sites-faciles)). Ces évolutions visent à fournir des outils plus précis, plus robustes et mieux adaptés aux besoins des agents et des citoyens.

## Sécurité
L'organisation a maintenu une vigilance accrue sur la protection des données et la correction de vulnérabilités :
- **Corrections de vulnérabilités critiques** : Résolution de failles de gestion de session dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) et de vulnérabilités dans [rdv-service-public](/repos/betagouv/rdv-service-public).
- **Renforcement des accès et protection des données** : Mise en place de protections contre les failles IDOR et CSRF dans [service-national-universitaire](/repos/betagouv/service-national-universitaire) et [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives). Amélioration de l'authentification (2FA) dans [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes) et sécurisation des processus d'authentification dans [stage-direct](/repos/betagouv/stage-direct).
- **Confidentialité et RGPD** : Efforts de masquage des données personnelles dans les logs pour [service-national-universitaire](/repos/betagouv/service-national-universitaire) et protection des données sensibles dans [zacharie](/repos/betagouv/zacharie).
- **Sécurisation des flux et téléchargements** : Renforcement de la validation des pièces jointes et de la sécurité des téléchargements dans [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice).
- **Audit et CI/CD** : Intégration d'outils d'analyse de sécurité automatique (Bandit, Checkov, Zizmor) dans les pipelines de [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes) et [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).

## Autres changements notables
- **Refontes architecturales et technologiques** : Migration vers FrankenPHP pour [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice) et passage à PostgreSQL/Dokku pour [turgot-fiches-collectivites](/repos/betagouv/turgot-fiches-collectivites).
- **Évolutions de la cartographie et des données SIG** : Mise à jour majeure des données réglementaires et de l'interface cartographique pour [nitrates](/repos/betagouv/nitrates), et intégration de nouvelles sources de données de logements pour [mle-back](/repos/betagouv/mle-back).
- **Modernisation des outils de gestion** : Introduction de la gestion par groupes et de nouveaux rôles de supervision dans [mon-service-securise](/repos/betagouv/mon-service-securise).

## Dépôts les plus actifs
- [transport-sanitaire](/repos/betagouv/transport-sanitaire) : Refonte complète de l'architecture (v10) et modernisation de l'interface utilisateur.
- [turgot-fiches-collectivites](/repos/betagouv/turgot-fiches-collectivites) : Changement d'identité (Fico), refonte technique et nouveaux formats d'export.
- [nitrates](/repos/betagouv/nitrates) : Amélioration de l'ergonomie cartographique et mise en conformité réglementaire.
- [portail-rse](/repos/betagouv/portail-rse) : Déploiement de la version 2 de l'analyse par intelligence artificielle.
- [mon-service-securise](/repos/betagouv/mon-service-securise) : Évolutions fonctionnelles majeures sur la gestion des périmètres et intégration CRM.
- [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives) : Travaux importants sur la sécurité et les nouveaux filtres d'administration.
