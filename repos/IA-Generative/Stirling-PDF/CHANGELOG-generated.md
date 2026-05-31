## Changelog : Stirling-PDF (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, Stirling-PDF a bénéficié d'améliorations significatives en termes de performance et de fonctionnalités, notamment l'optimisation du chargement de certaines parties de l'interface utilisateur pour réduire la taille des "chunks" générés par Vite, et des avancées dans l'intégration d'un système RAG (Retrieval-Augmented Generation) pour l'IA. Des corrections de bugs ont également été apportées pour améliorer l'expérience utilisateur, comme la correction du bouton de déplacement d'outils et l'indicateur de sauvegarde sur le bureau.

### Évolutions fonctionnelles
- Correction du bouton de déplacement dans la barre d'outils multi-outils [#6291](https://github.com/IA-Generative/Stirling-PDF/issues/6291).
- Ajout d'un indicateur de sauvegarde sur le bureau lors de l'enregistrement de fichiers [#6310](https://github.com/IA-Generative/Stirling-PDF/issues/6310).
- Intégration initiale d'un système RAG (Retrieval-Augmented Generation) pour l'IA, permettant d'informer le moteur d'IA des endpoints désactivés sur le backend [#6251](https://github.com/IA-Generative/Stirling-PDF/issues/6251) et développement plus poussé [#6197](https://github.com/IA-Generative/Stirling-PDF/issues/6197).
- Développement d'un agent pour les commentaires PDF [#6196](https://github.com/IA-Generative/Stirling-PDF/issues/6196).

### Évolutions techniques
- Optimisation du chargement de certaines parties de l'interface utilisateur en utilisant l'importation paresseuse (lazy import) pour améliorer la taille des "chunks" générés par Vite [#6278](https://github.com/IA-Generative/Stirling-PDF/issues/6278).
- Mise à jour de plusieurs dépendances et librairies utilisées dans le projet (voir section "Autres changements" pour plus de détails).
- Mise à jour de l'image Docker de base avec une version plus récente de Eclipse Temurin [#6292](https://github.com/IA-Generative/Stirling-PDF/issues/6292) et [#6293](https://github.com/IA-Generative/Stirling-PDF/issues/6293).

### Autres changements
- Configuration de Dependabot pour gérer les mises à jour de groupes de dépendances frontend npm et cargo [#6287](https://github.com/IA-Generative/Stirling-PDF/issues/6287).
- Mises à jour de nombreuses dépendances, notamment : springSecuritySamlVersion, embedpdf, tauri, sha2, windows, globals, step-security/harden-runner, mui, com.google.guava:guava, actions/setup-node, org.springdoc:springdoc-openapi-starter-webmvc-ui, actions/upload-artifact, actions/github-script, gradle/actions. Ces mises à jour sont gérées par Dependabot et visent à maintenir la sécurité et la stabilité du projet.
