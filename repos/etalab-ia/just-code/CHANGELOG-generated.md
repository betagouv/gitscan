## Changelog : just-code (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois a marqué une étape majeure avec la transition de l'outil vers une version entièrement développée en Go, remplaçant les anciens scripts par un binaire unique et plus robuste. Le projet a considérablement élargi sa compatibilité en intégrant un support complet pour Windows et en ajoutant de nouveaux environnements d'exécution (macOS et Lima). La sécurité a également été renforcée par l'ajout de contrôles automatiques pour empêcher l'utilisation de secrets dans les espaces de travail.

### Évolutions fonctionnelles
- **Support de Windows :** Compatibilité étendue via le runtime Microsandbox, incluant des correctifs pour la gestion des chemins et des processus sous Windows.
- **Nouveaux environnements d'exécution :** 
    - Ajout du runtime `agent-vm` basé sur Lima.
    - Ajout du runtime macOS via Tart, permettant l'exécution d'environnements Xcode.
- **Sécurité des données :** Le démarrage est désormais refusé si des secrets sont détectés dans l'espace de travail [#42](https://github.com/etalab-ia/just-code/issues/42).
- **Amélioration de l'expérience CLI :** Ajout d'une commande `version` et alignement de l'interface sur la version TypeScript.

### Évolutions techniques
- **Refonte logicielle (Portage Go) :** Migration complète de la logique de gestion des runtimes (Docker, Microsandbox, Tart) vers le langage Go, permettant la suppression des dépendances aux scripts shell et au `justfile`.
- **Optimisation du déploiement :** Intégration directe des ressources de runtime à l'intérieur du binaire Go pour simplifier l'installation.
- **Sécurité et Intégrité :**
    - Mise en place de la vérification d'attestation pour garantir l'intégrité des composants [#40](https://github.com/etalab-ia/just-code/issues/40).
    - Intégration d'un hook de pré-commit (Gitleaks) pour prévenir les fuites de secrets.
- **Simplification de l'architecture :** Suppression progressive du runtime Docker au profit de solutions d'isolation plus modernes (Microsandbox, Tart, Lima).
- **CI/CD et Release :** 
    - Automatisation du versionnage et de la publication des binaires via `release-please`.
    - Optimisation des workflows de build, notamment pour les artefacts macOS.

### Autres changements
- **Documentation :** Refonte complète du README pour mieux accompagner l'utilisateur dans son parcours et ajout de guides de démarrage rapide pour Windows.
- **Nettoyage :** Suppression des anciens workflows de CI et des commandes de build obsolètes.
