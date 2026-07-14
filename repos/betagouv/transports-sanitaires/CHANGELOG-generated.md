## Changelog : transports-sanitaires (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, le simulateur de transport sanitaire a connu une refonte majeure. L'application d'identification et le simulateur ont été fusionnés en une seule application, avec l'ajout de nouvelles fonctionnalités d'identification et de traçage via Matomo. L'architecture a été revue et documentée, et un workflow CI/CD a été mis en place pour automatiser les tests et le déploiement. De nouvelles règles ont également été intégrées au simulateur.

### Évolutions fonctionnelles
- Ajout d'un bouton "Précédent" pour revenir au formulaire depuis les résultats du simulateur.
- Implémentation d'un workflow d'identification avec capture du nom et prénom, même pour les services "autres".
- Intégration de Matomo pour le suivi pseudonymisé des événements (funnel événementiel) et du contexte prescripteur.
- Possibilité d'alimenter Grist avec les saisies libres de l'identification.
- Adaptation de l'application aux nouvelles versions des règles de calcul.
- Ajout d'un raccourci clavier pour ouvrir la fenêtre d'aide (glossaire).
- Amélioration de l'accessibilité avec un focus automatique sur l'input lors de l'ouverture de la fenêtre d'aide.
- Extension pour faciliter la recherche dans le glossaire.

### Évolutions techniques
- Fusion de l'application d'identification et du simulateur en une seule application.
- Refactor de l'identification avec une meilleure organisation des modules et un langage plus clair.
- Passage à un backend Express avec un référentiel Grist pour l'identification.
- Mise en place d'un workflow GitHub Actions pour les tests et le build.
- Documentation de l'architecture avec des diagrammes Mermaid et des ADR (Architecture Decision Records).
- Utilisation de Scalingo pour le backend au lieu d'une fonction FaaS.
- Fusion des règles Publicodes en un seul fichier.
- Migration vers un nouveau système de gestion de projet (Notion).
- Configuration de l'outil `mise` pour la gestion des dépendances et des tâches.

### Autres changements
- Ajout d'un script de validation des règles Publicodes.
- Suppression de fichiers obsolètes.
- Mise à jour de la documentation (AGENTS.md, diagrammes d'architecture).
- Inclusion de la version du `package.json` dans le nom du zip du glossaire.
- Correction des erreurs TypeScript.
- Déploiement sur GitHub Pages.
- Suppression de la versionnage des fichiers `.tsbuildinfo`.
- Ajout de la configuration pour `serve` en dépendance de déploiement.
- Renommage de l'application en `simulateur-eligibilite`.
- Initialisation du dépôt avec un premier commit.
