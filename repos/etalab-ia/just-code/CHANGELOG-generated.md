## Changelog : just-code (30 derniers jours, au 04 novembre 2026)

### Résumé
Ce mois-ci, just-code a franchi une étape majeure dans la maturation de son expérience utilisateur. L'assistant de configuration initiale (wizard) a été entièrement repensé pour être plus interactif et intuitif, facilitant le choix des modèles d'IA et la configuration des accès GitHub. La gestion de la sécurité a également été renforcée, notamment par l'introduction d'un système de consentement pour les statistiques et une meilleure gestion des secrets de projet.

### Évolutions fonctionnelles
- **Assistant de configuration (Wizard) :** Refonte complète de l'interface d'initialisation via l'outil `huh`, offrant un parcours plus fluide pour la sélection des compétences (skills) [#167], des modèles d'IA et la configuration des accès GitHub [#169].
- **Gestion des modèles :** Introduction du modèle Ministral comme option de petit modèle OpenCode et support de la sélection multi-modèles lors de l'installation.
- **Gestion des secrets et credentials :** 
    - Possibilité d'importer des secrets de projet via des fichiers `.env`.
    - Amélioration de la visibilité et de la gestion du statut des clés API (notamment Albert API).
- **Expérience de fin de session :** Ajout d'un écran de fin de session permettant de visualiser et de récupérer les modifications de travail effectuées.
- **Statistiques d'usage :** Mise en place d'un mécanisme de consentement explicite avant toute collecte de statistiques.
- **Importation :** Ajout de la capacité d'importer des projets existants depuis Albert Code.
- **Interface TUI :** Améliorations de la navigation et de l'affichage (gestion du curseur, comportement lors du redimensionnement de la fenêtre, affichage des listes de sélection).

### Évolutions techniques
- **Infrastructure et Runtime :** 
    - Mises à jour successives du runtime Microsandbox (jusqu'à la version 0.7.13).
    - Amélioration de la configuration et de la détection des ports invités (guest ports).
- **Sécurité et Intégrité :** 
    - Renforcement de la protection des secrets via le transport natif et le proxy Microsandbox.
    - Amélioration des mécanismes de vérification des empreintes (digests) pour garantir l'intégrité des fichiers gérés.
- **Gestion de l'espace de travail :** Optimisation de la synchronisation de l'espace de travail et de la détection des réversions ou modifications de l'hôte.
- **Qualification et Tests :** Travail intensif sur les pipelines de qualification pour fournir des preuves de fonctionnement robustes sur macOS, Linux (amd64/arm64) et Windows.

### Autres changements
- **Documentation :** Restructuration de la documentation en pages thématiques et enrichissement des guides concernant la sécurité et la gestion des secrets.
- **Nettoyage :** Optimisation des processus de CI/CD et des scripts de test.
