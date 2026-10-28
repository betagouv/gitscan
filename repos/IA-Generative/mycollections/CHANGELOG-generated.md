## Changelog : mycollections (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois a marqué une transformation majeure de la plateforme avec l'introduction des "Assistants de recherche" (Chat MirAI) et une intégration poussée de nouvelles sources de données comme Résana et Google Drive. L'expérience utilisateur a été largement simplifiée grâce à un nouveau parcours de création guidé et à une meilleure visibilité sur la qualité des documents indexés.

### Évolutions fonctionnelles
- **Nouveaux Assistants de recherche :** Création, gestion et test d'assistants via un assistant de création en 5 étapes, incluant un mode "bac à sable" pour tester les réponses et un système d'archivage.
- **Intégration Résana :** Connexion simplifiée avec reprise automatique de session, sélection de périmètre par dossiers et support d'imports massifs (jusqu'à 20 000 documents).
- **Gestion des fichiers (Drive) :** Possibilité d'importer et de synchroniser des dossiers Google Drive avec un contrôle de la sensibilité des documents.
- **Contrôle Qualité :** Suivi détaillé de l'indexation permettant de détecter les documents tronqués, l'utilisation de l'OCR ou les fichiers vides.
- **Interface Utilisateur (UI) :** 
    - Refonte de l'accueil (vue compacte et tuiles).
    - Nouveau catalogue avec tri, gestion des avis usagers et fonctions d'archivage.
    - Fiches de collections enrichies (onglets pour l'historique, les métadonnées et les consignes).
- **Recherche :** Amélioration de la recherche via l'API MirAI et meilleure lisibilité des titres de sections.

### Évolutions techniques
- **Moteur d'indexation :** Refactorisation vers une interface générique et intégration de Gotenberg pour la conversion automatique des formats bureautiques en PDF.
- **Architecture & Modèles :** Généralisation de l'utilisation de modèles Pydantic pour sécuriser les échanges de données (indexation, qualité, assistants).
- **Sécurité & Authentification :** 
    - Correction de vulnérabilités critiques (Nginx, certifi, pillow).
    - Amélioration de la gestion des sessions (renouvellement automatique des jetons pour éviter les déconnexions intempestives).
- **Infrastructure & CI/CD :** Mise en place de déploiements via ArgoCD/Helm et renforcement massif de la couverture de tests de bout en bout (E2E).
- **Protocoles :** Introduction d'un serveur MCP (Model Context Protocol) pour exposer les outils des assistants.

### Autres changements
- **Documentation :** Mise à jour complète de la documentation technique (API Résana, guides de décision/ADR) et des manuels utilisateurs.
- **Qualité du code :** Intégration de contrôles de type et de linting (commitlint, frontend type-check) dans la chaîne de CI.
