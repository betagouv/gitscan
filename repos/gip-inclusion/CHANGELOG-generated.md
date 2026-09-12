# Synthèse d'activité : gip-inclusion (du 26/06 au 10/09)

## Résumé de l'activité
L'activité de cette période est marquée par une montée en puissance des outils de mise en relation et de gestion de parcours. Le rebranding vers "Match Europe" pour [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) et l'enrichissement des fonctionnalités de suivi dans [les-emplois](/repos/gip-inclusion/les-emplois) permettent aux professionnels de mieux accompagner les candidats. Parallèlement, les plateformes [le-marche](/repos/gip-inclusion/le-marche) et [traiteurs-engages-app](/repos/gip-inclusion/traiteurs-engages-app) améliorent l'expérience des acheteurs et des administrateurs grâce à de nouveaux outils de recherche, de gestion de devis et de communication enrichie.

Sur le plan technique, l'organisation franchit des étapes clés de modernisation pour garantir la scalabilité et la fiabilité des services. Cela se traduit par des migrations majeures vers des architectures plus robustes (Django, Airflow 3, conteneurs serverless) et une amélioration constante de l'intelligence des données pour offrir des résultats de recherche plus pertinents.

## Sécurité
- Renforcement de la sécurité des accès et des données via la correction de vulnérabilités dans [immersion-facile](/repos/gip-inclusion/immersion-facile) et la restriction du téléchargement de listes aux utilisateurs authentifiés dans [le-marche](/repos/gip-inclusion/le-marche).
- Amélioration de la gestion des secrets avec la suppression de mots de passe codés en dur dans [fluo-proto](/repos/gip-inclusion/fluo-proto).
- Mise en place d'une politique de sécurité (CSP) pour sécuriser l'intégration en iframe dans [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil).
- Application de correctifs de sécurité sur l'infrastructure d'orchestration dans [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow).

## Autres changements notables
- **Migrations d'infrastructure majeures** : Passage à Airflow 3 pour [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow), migration vers une architecture Django complète pour [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) et refonte massive de l'architecture de données vers le framework `di_v1` pour [dora](/repos/gip-inclusion/dora).
- **Évolutions structurelles et déploiement** : Transition vers un modèle de déploiement en conteneurs serverless pour [fluo-proto](/repos/gip-inclusion/fluo-proto), changement de la base de données source pour [autometa](/repos/gip-inclusion/autometa) et mise en place de la conteneurisation Docker pour [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil).

## Dépôts les plus actifs
- [les-emplois](/repos/gip-inclusion/les-emplois) : Refonte majeure de la gestion des accompagnements et des parcours candidats.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding vers Match Europe et nouveaux outils de matching et d'analytics.
- [autometa](/repos/gip-inclusion/autometa) : Amélioration de la personnalisation, de la robustesse de l'infrastructure et de la chaîne CI/CD.
- [dora](/repos/gip-inclusion/dora) : Migration massive de l'architecture de données et optimisation des performances.
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Refonte visuelle complète et migration vers une architecture Django.
