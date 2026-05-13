## Changelog : dictaphone (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, en particulier sur l'application mobile, avec l'ajout de fonctionnalités clés comme la gestion des téléchargements, la suppression de fichiers, et l'authentification sécurisée. Des améliorations significatives ont également été apportées à l'interface web, notamment la gestion des transcriptions et l'intégration avec des services externes comme Docs.

### Évolutions fonctionnelles
- **Mobile :**
    - Amélioration de l'expérience utilisateur lors de la réinitialisation du mot de passe.
    - Affichage plus clair des raisons de blocage des téléchargements.
    - Ajout de la possibilité de télécharger uniquement via Wifi.
    - Amélioration du retour haptique.
    - Amélioration de la détection de la connexion réseau.
    - Amélioration de l'accessibilité des éléments interactifs.
    - Ajout d'une barre de progression pour les téléchargements.
    - Possibilité de sélectionner le texte de la transcription.
    - Ajout d'un lien pour supprimer le compte utilisateur.
    - Correction de bugs liés au comportement de l'enregistrement et de la suppression de fichiers.
    - Mise en place d'une authentification plus robuste avec JWT et PKCE.
    - Ajout de la possibilité de partager et d'ouvrir la transcription dans Docs.
- **Web :**
    - Ajout d'une option pour réessayer les téléchargements échoués.
    - Amélioration de l'affichage des transcriptions groupées par intervenant.
    - Ajout d'un bouton pour copier la transcription dans le presse-papier.
    - Nouvelle interface utilisateur pour la gestion des enregistrements, incluant la suppression et la consultation des détails.
    - Ajout d'une page d'accueil standardisée.
    - Possibilité de télécharger l'application mobile.
- **Général :**
    - Ajout d'une commande pour nettoyer les fichiers temporaires et supprimés.
    - Cette commande est maintenant exécutée régulièrement via un cronjob.
    - Support vidéo activé par défaut.

### Évolutions techniques
- **Authentification :** Mise à jour de la logique JWT et PKCE pour une meilleure sécurité.
- **Backend :**
    - Amélioration de la gestion des variables d'environnement pour la redirection SSL.
    - Amélioration de la gestion des erreurs et des logs.
    - Exposition de l'ID de l'application Docs pour l'intégration.
    - Support amélioré pour les fichiers audio/webm.
    - Augmentation de la taille maximale des fichiers uploadés.
- **Frontend :**
    - Refactorisation du code pour une meilleure organisation et maintenabilité.
    - Amélioration des performances.
    - Mise à jour des dépendances.
- **CI/CD :**
    - Généralisation des tests backend.
    - Ajout de tests linting et de vérification du changelog (temporairement désactivés).
    - Poussée des images Docker sur les branches d'intégration.
- **Mobile :**
    - Mise à jour des dépendances iOS.
    - Refactorisation du code pour une meilleure organisation.
    - Intégration de PostHog pour l'analyse.

### Autres changements
- Mise à jour de la documentation.
- Correction de fautes de frappe et amélioration de la qualité du code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Mise à jour des logos et des icônes.
- Suppression de l'écriture inclusive dans la documentation française.
- Publication des versions 0.5.0, 0.5.1, 0.5.2, 0.5.3, 0.5.4 (backend/frontend), 1.0.0 (mobile), 1.0.1 (mobile), 1.0.2 (mobile) et 1.0.3 (mobile).
