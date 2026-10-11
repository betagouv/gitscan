## Changelog : ocr (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur grâce à une nouvelle interface de gestion des tâches et l'extension des outils de développement avec de nouveaux SDK. Le projet a également franchi une étape importante en matière de sécurité et de robustesse, notamment via une gestion plus fine de l'authentification, une automatisation du nettoyage des données et une sécurisation accrue des conteneurs.

### Évolutions fonctionnelles
- **Nouvelle interface client** : Passage de l'affichage des tâches d'un format tableau à une vue en grille de tuiles ([ec15ade](https://github.com/IA-Generative/ocr/commit/ec15ade)).
- **Amélioration de l'ergonomie** : Ajout d'un bouton de rafraîchissement manuel pour l'onglet des tâches ([f048142](https://github.com/IA-Generative/ocr/commit/f048142)) et correction de la pagination de la liste des tâches ([ef3737b](https://github.com/IA-Generative/ocr/commit/ef3737b)).
- **Extension des SDK** : 
    - Création d'un nouveau SDK TypeScript/Node.js ([c3b5db2](https://github.com/IA-Generative/ocr/commit/c3b5db2)).
    - Mise à jour du SDK Python avec synchronisation des schémas API et ajout de la méthode `login()` ([56b9d29](https://github.com/IA-Generative/ocr/commit/56b9d29)).
- **Authentification enrichie** : 
    - Support complet des jetons de rafraîchissement (refresh tokens) ([9a474ae](https://github.com/IA-Generative/ocr/commit/9a474ae)).
    - Ajout de clés API pour permettre l'authentification de machine à machine ([96e9c4e](https://github.com/IA-Generative/ocr/commit/96e9c4e)).
    - Mise à disposition d'un endpoint de mot de passe pour les clients non-navigateurs ([8777993](https://github.com/IA-Generative/ocr/commit/8777993)).

### Évolutions techniques
- **Fiabilité du traitement OCR** : Correction d'un bug entraînant la perte des pages suivantes (page 2+) lors du traitement de documents multi-pages (DOCX, PPTX, etc.) ([d8ce56a](https://github.com/IA-Generative/ocr/commit/d8ce56a)).
- **Optimisation du backend** : Mise en place d'un nettoyage périodique automatique des anciennes tâches via Celery Beat ([3ac5dee](https://github.com/IA-Generative/ocr/commit/3ac5dee)).
- **Sécurité renforcée** :
    - Implémentation de la limitation de débit (rate-limiting) sur l'endpoint de connexion ([0905ab9](https://github.com/IA-Generative/ocr/commit/0905ab9)).
    - Renforcement de la protection CSRF lors de la déconnexion et meilleure gestion des sessions Keycloak ([0d3bf39](https://github.com/IA-Generative/ocr/commit/0d3bf39), [b4f16a2](https://github.com/IA-Generative/ocr/commit/b4f16a2)).
    - Sécurisation des conteneurs par l'utilisation d'utilisateurs non-root et le support d'UID arbitraires ([8fb66d5](https://github.com/IA-Generative/ocr/commit/8fb66d5), [f9e2807](https://github.com/IA-Generative/ocr/commit/f9e2807)).
- **Infrastructure et CI/CD** :
    - Création d'une image Docker dédiée aux migrations de données ([038f606](https://github.com/IA-Generative/ocr/commit/038f606)).
    - Optimisation des builds Docker (ajout de `HEALTHCHECK` et réduction du contexte de build) ([e83b97b](https://github.com/IA-Generative/ocr/commit/e83b97b), [627c743](https://github.com/IA-Generative/ocr/commit/627c743)).
    - Refonte complète de l'outillage de développement et du workflow de contribution ([4dcbc11](https://github.com/IA-Generative/ocr/commit/4dcbc11)).
    - Amélioration de la gestion des Helm charts et de la distribution des images via GHCR ([6d2b06e](https://github.com/IA-Generative/ocr/commit/6d2b06e41da1dedd74b7b37fd107e6ba0770a572)).
- **Simplification du pipeline** : Suppression de l'étape d'extraction de formulaires basée sur les LLM ([8f4d8c4](https://github.com/IA-Generative/ocr/commit/8f4d8c4)).

### Autres changements
- **Documentation** : 
    - Enrichissement de la documentation de l'API avec des descriptions détaillées des routes ([996be69](https://github.com/IA-Generative/ocr/commit/996be69)).
    - Ajout d'un guide de configuration de la console d'administration Keycloak pour le flux BFF ([e89ca09](https://github.com/IA-Generative/ocr/commit/e89ca09)).
    - Mise à jour des liens du dépôt et de la documentation sur les registres d'images ([3ec5b35](https://github.com/IA-Generative/ocr/commit/3ec5b35), [dd84021](https://github.com/IA-Generative/ocr/commit/dd84021)).
- **Nettoyage** : Suppression de la fonctionnalité de transcription YouTube et de la dépendance `yt-dlp` ([69fe10a](https://github.com/IA-Generative/ocr/commit/69fe10a)).
