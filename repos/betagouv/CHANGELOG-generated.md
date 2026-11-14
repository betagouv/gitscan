# Synthèse d'activité : betagouv (du 01/10 au 15/11)

## Résumé de l'activité
L'activité de l'organisation est marquée par des lancements majeurs et des montées en version significatives qui améliorent l'expérience utilisateur et la puissance des outils. Plusieurs projets franchissent des étapes clés, comme l'application [pnm](/repos/betagouv/pnm) qui devient pleinement fonctionnelle ou le lancement de la première version stable de [slack2tchap](/repos/betagouv/slack2tchap). L'intelligence artificielle progresse également avec le déploiement de l'analyse de nouvelle génération sur le [portail-rse](/repos/betagouv/portail-rse).

Les utilisateurs bénéficient de parcours simplifiés et plus intuitifs, notamment grâce à l'automatisation du pré-remplissage des dossiers dans [pass-sport](/repos/betagouv/pass-sport) ou à l'intégration de nouvelles fonctionnalités cartographiques dans [nitrates](/repos/betagouv/nitrates) et [sylvasan](/repos/betagouv/sylvasan). L'alignement sur les standards de design de l'État (DSFR) se généralise, garantissant une interface cohérente et accessible sur l'ensemble des services.

## Sécurité
- **Correction de vulnérabilités** : Résolution de failles critiques, notamment sur la gestion des sessions dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) et la mise à jour de dépendances sensibles dans [mon-profil-anssi](/repos/betagouv/mon-profil-anssi) et [rdv-service-public](/repos/betagouv/rdv-service-public).
- **Renforcement des accès** : Amélioration de l'authentification (2FA, OAuth2) et protection contre les failles de type IDOR ou CSRF dans [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes), [reva](/repos/betagouv/reva) et [service-national-universel](/repos/betagouv/service-national-universel).
- **Automatisation de la sécurité** : Intégration de nouveaux outils d'analyse de vulnérabilités (Bandit, checkov, zizmor) dans les processus de développement de [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes) et [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).
- **Protection des données** : Renforcement de la confidentialité et du respect du RGPD (masquage des données dans les logs) dans [service-national-universel](/repos/betagouv/service-national-universel) et [recoco-sync](/repos/betagouv/recoco-sync).

## Autres changements notables
- **Migrations d'infrastructure** : Passage à FrankenPHP pour [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice) et migration vers PostgreSQL et Dokku pour [turgot-fiches-collectivites](/repos/betagouv/turgot-fiches-collectivites).
- **Évolutions technologiques majeures** : Montées de versions importantes des environnements (Node.js 26, PostgreSQL 18, Ruby 3.4) pour [mon-service-securise](/repos/betagouv/mon-service-securise) et [referentiel-agrements-assistants-maternels-familiaux](/repos/betagouv/referentiel-agrements-assistants-maternels-familiaux).
- **Refontes architecturales** : Intégration du moteur de décision Publicodes dans [transport-sanitaire](/repos/betagouv/transport-sanitaire) et restructuration profonde du système de [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives).

## Dépôts les plus actifs
- [transport-sanitaire](/repos/betagouv/transport-sanitaire) : Montée en version majeure avec l'intégration du modèle de règles v10 et une refonte de l'interface.
- [turgot-fiches-collectivites](/repos/betagouv/turgot-fiches-collectivites) : Rebranding complet vers "Fico" et refonte profonde de l'architecture et des formats d'export.
- [nitrates](/repos/betagouv/nitrates) : Mise à jour majeure de l'interface cartographique et intégration de nouvelles données réglementaires.
- [portail-rse](/repos/betagouv/portail-rse) : Lancement de l'analyse par intelligence artificielle v2 et nouvelles capacités d'export.
- [mon-service-securise](/repos/betagouv/mon-service-securise) : Automatisation de la génération de supports de commission et gestion des risques.
- [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives) : Amélioration de l'expérience utilisateur, de la gestion documentaire et de la sécurité.
