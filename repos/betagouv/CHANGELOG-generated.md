# Synthèse d'activité : betagouv (du 01/09 au 08/09/2026)

## Résumé de l'activité
L'activité de cette période est marquée par une intégration croissante de l'intelligence artificielle dans les outils de conseil et de création de contenu ([science-infuse](/repos/betagouv/science-infuse), [portail-rse-externe](/repos/betagouv/portail-rse-externe), [mon-entreprise](/repos/betagouv/mon-entreprise)). Plusieurs plateformes ont franchi des étapes clés, notamment avec le lancement de la gestion des VAE collectives ([reva](/repos/betagouv/reva)), l'ouverture d'un espace dédié aux étudiants ([monlogementetudiant](/repos/betagouv/monlogementetudiant)) ou encore la première version stable d'un connecteur de données ([slack2tchap](/repos/betagouv/slack2tchap)).

Parallèlement, un effort soutenu a été porté sur l'amélioration de l'expérience utilisateur et la conformité aux standards de l'État. De nombreux projets ont affiné leurs interfaces, simplifié leurs parcours de saisie ou optimisé leur accessibilité, tout en renforçant la robustesse de leurs infrastructures respectives ([nitrates](/repos/betagouv/nitrates), [ma-cantine](/repos/betagouv/ma-cantine), [sylvasan](/repos/betagouv/sylvasan)).

## Sécurité
- Correction de vulnérabilités critiques de type IDOR et renforcement de la politique de sécurité du contenu (CSP) pour [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives).
- Correction d'une vulnérabilité de sécurité liée à la gestion des sessions sur [mon-suivi-justice](/repos/betagouv/mon-suivi-justice).
- Renforcement de la protection des données via l'ajout d'un WAF (Web Application Firewall) et de headers de sécurité sur [seves](/repos/betagouv/seves).
- Mise en œuvre de la norme RFC 9116 via l'ajout du fichier `security.txt` sur [nitrates](/repos/betagouv/nitrates).
- Intégration d'outils d'analyse de configuration pour prévenir les vulnérabilités dans les pipelines CI/CD sur [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).

## Autres changements notables
- **Migrations technologiques majeures** : Passage vers Rails 8 ([rdv-service-public](/repos/betagouv/rdv-service-public)), vers PHP 8.5 et Symfony 8.1 ([mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice)), et vers Vite 8 ([lab-anssi-ui-kit](/repos/betagouv/lab-anssi-ui-kit)).
- **Évolutions architecturales** : Intégration d'un nouveau moteur d'IA (v2) ([portail-rse-externe](/repos/betagouv/portail-rse-externe)), refonte du système de gestion des droits par rôles ([reva](/repos/betagouv/reva)) et migration du centre de notifications vers TypeScript ([mon-service-securise](/repos/betagouv/mon-service-securise)).
- **Infrastructure** : Initialisation de l'infrastructure en tant que code (IaC) pour le projet [nitrates-iac](/repos/betagouv/nitrates-iac).

## Dépôts les plus actifs
- [zacharie](/repos/betagouv/zacharie) : Optimisation importante du processus de vente/don et des communications par email.
- [sylvasan](/repos/betagouv/sylvasan) : Améliorations de la saisie de données terrain, de la cartographie et de la gestion des images.
- [seves](/repos/betagouv/seves) : Évolutions majeures sur le module de Santé Animale et nouveaux outils de pilotage.
- [reva](/repos/betagouv/reva) : Déploiement des fonctionnalités de gestion des VAE Collectives et refonte de l'API.
- [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives) : Sécurisation massive de la plateforme et optimisation des performances.
- [mon-entreprise](/repos/betagouv/mon-entreprise) : Introduction d'un comparateur de modèles juridiques et intégration des spécificités de Mayotte.
- [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice) : Refonte technique majeure et amélioration de la gestion documentaire.
