# Synthèse d'activité : datagouv (du 01/10 au 07/10)

## Résumé de l'activité
L'activité récente est marquée par une amélioration significative de l'expérience utilisateur et une mise à jour massive des données de référence. Les outils de gestion de processus comme [passemarche](/repos/datagouv/passemarche) et [hubee](/repos/datagouv/hubee) ont été enrichis pour offrir des parcours de candidature plus fluides et une gestion documentaire plus complète. Parallèlement, l'écosystème bénéficie d'une actualisation importante des données géographiques, cadastrales et de découpage administratif, garantissant la fiabilité des informations disponibles.

L'organisation poursuit également sa modernisation technique avec la refonte de l'interface de ligne de commande [datagouv-cli](/repos/datagouv/datagouv-cli) et l'évolution des capacités d'évaluation de l'IA dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation). Ces évolutions visent à fournir des outils plus robustes, performants et faciles à intégrer pour les développeurs et les administrations.

## Sécurité
- **Renforcement de l'accès et des jetons** : déploiement de l'introspection de jetons et du contrôle d'accès par adresse IP dans [apistration](/repos/datagouv/apistration).
- **Protection de la vie privée** : amélioration de l'anonymisation des données sensibles (adresses email, dates et lieux de naissance) dans les logs et les outils d'évaluation ([roles.data](/repos/datagouv/roles.data), [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation), [apistration](/repos/datagouv/apistration)).
- **Sécurisation de l'infrastructure** : utilisation de bases Docker "distroless" pour les images de production dans [hubee](/repos/datagouv/hubee).

## Autres changements notables
- **Migrations et modernisation des stacks** : passage à Rails 8.1 pour [relais](/repos/datagouv/relais), adoption de PNPM pour [ouverture.data.gouv.fr](/repos/datagouv/ouverture.data.gouv.fr) et [grist-plugin-opendata](/repos/datagouv/grist-plugin-opendata), et migration vers Vite pour ce dernier.
- **Refonte d'outils de développement** : migration de l'interface en ligne de commande de [datagouv_client](/repos/datagouv/datagouv_client) vers un dépôt dédié [datagouv-cli](/repos/datagouv/datagouv-cli), permettant une distribution autonome sur Windows et macOS.
- **Évolutions architecturales majeures** : introduction d'une couche sémantique pour l'évaluation de l'IA dans [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) et migration vers `Solid Queue` pour la gestion des tâches de fond dans [simplifions](/repos/datagouv/simplifions).

## Dépôts les plus actifs
- [passemarche](/repos/datagouv/passemarche) : refonte du parcours de candidature (choix du mode, wizard de navigation).
- [apistration](/repos/datagouv/apistration) : intégration de DataPass et renforcement de la sécurité des jetons.
- [datagouv-cli](/repos/datagouv/datagouv-cli) : migration majeure du code CLI et support multi-plateforme.
- [hubee](/repos/datagouv/hubee) : transition vers le concept de "télédossiers" et enrichissement de la gestion documentaire.
- [datagouv-ai-evaluation](/repos/datagouv/datagouv-ai-evaluation) : refonte structurelle profonde et ajout de capacités d'évaluation sémantique.
- [relais](/repos/datagouv/relais) : mise à jour majeure de l'infrastructure (Rails 8.1) et intégration CNOUS.
