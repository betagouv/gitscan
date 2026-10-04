## Changelog : ocr-api (30 derniers jours, au 2 octobre 2026)

### Résumé
Ce mois-ci, l'API a connu une évolution majeure centrée sur l'amélioration de l'expérience utilisateur et le renforcement de la sécurité. L'interface de gestion des tâches a été modernisée, un nouveau SDK pour Node.js/TypeScript a été introduit, et la sécurité des accès (authentification machine-to-machine et gestion des sessions) a été considérablement consolidée. Parallèlement, l'infrastructure a été optimisée pour une meilleure stabilité et un nettoyage automatique des données.

### Évolutions fonctionnelles
- **Nouvelle interface utilisateur (Client) :**
    - Passage d'un affichage des tâches sous forme de tableau à une grille de tuiles plus visuelle.
    - Ajout d'un bouton de rafraîchissement manuel pour la liste des tâches.
    - Amélioration de la pagination de la liste des tâches utilisateur.
    - Ajout de liens directs vers la documentation de l'API et le dépôt GitHub dans le pied de page.
- **Nouveaux outils de développement :**
    - Lancement d'un SDK officiel TypeScript/Node.js pour faciliter l'intégration.
- **Améliorations du traitement :**
    - Correction d'un bug entraînant la perte des pages suivantes (page 2+) lors du traitement de documents multi-pages (DOCX, PPTX, etc.).
    - Support de la disponibilité GPU.

### Évolutions techniques
- **Sécurité et Authentification :**
    - Introduction des clés API pour permettre l'authentification de type "machine-to-machine".
    - Ajout d'un endpoint de jeton (token) avec support du "password-grant" pour les clients non-navigateurs.
    - Implémentation du support des jetons de rafraîchissement (refresh tokens) de bout en bout.
    - Renforcement de la sécurité des sessions : fin de session Keycloak lors de la déconnexion et protection contre les attaques CSRF sur la déconnexion.
    - Mise en place d'une limitation de débit (rate-limiting) sur l'endpoint de connexion par IP client.
    - Durcissement des conteneurs : passage à des utilisateurs non-root, application de correctifs de sécurité (notamment sur `libexpat` [CVE-2026-93990](https://github.com/IA-Generative/ocr-api/commit/5641a9d)) et mise à jour des paquets de base ([#469](https://github.com/IA-Generative/ocr-api/issues/469)).
- **Optimisation du Backend et Pipeline :**
    - Automatisation du nettoyage périodique des tâches obsolètes via Celery Beat.
    - Suppression de l'extraction OCR/formulaire basée sur les LLM pour simplifier le pipeline.
    - Refactorisation du SDK Python vers un répertoire dédié (`sdk/python`).
- **Infrastructure et CI/CD :**
    - Migration de l'environnement de build vers Node 24 LTS et pnpm 11.
    - Remplacement de l'image de stockage Minio par RustFS.
    - Optimisation des Dockerfiles (ajout de `HEALTHCHECK`, optimisation du contexte de build, installation déterministe d'OpenCV).
    - Amélioration de la chaîne CI/CD (automatisation de la synchronisation des branches et gestion des tokens GitHub App).

### Autres changements
- **Documentation :**
    - Ajout d'un guide de configuration de la console d'administration Keycloak pour le flux BFF.
    - Amélioration de la documentation de l'API (descriptions des routes et tags).
    - Mise à jour de la documentation de sécurité.
- **Nettoyage :**
    - Suppression de la dépendance YouTube/yt-dlp et des méthodes SDK associées.
    - Suppression de modules d'infrastructure inutilisés et nettoyage des fichiers de configuration `.env.example`.
