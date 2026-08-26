## Changelog : grist-custom-forms (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois a été marqué par une transition majeure de l'identité visuelle vers "Match Europe" et un renforcement significatif des capacités de suivi. Le projet a intégré de nouveaux outils d'analyse de données (analytics) et a considérablement amélioré la gestion des mises en relation (matchings), notamment pour les profils atypiques et les candidatures spontanées.

### Évolutions fonctionnelles
- **Identité et Interface (Match Europe & EURES) :**
    - Rebranding complet des pages publiques EURES vers l'identité "Match Europe".
    - Refonte de l'interface d'administration pour une meilleure ergonomie.
    - Amélioration de la lisibilité des offres d'emploi et des suivis de non-matching.
    - Optimisation de l'affichage : listes de matching compactes, badges de statut clarifiés et utilisation de la pleine largeur pour les métriques.
- **Gestion des Matchings :**
    - Introduction de la gestion des "borderline matchings" (mises en relation limites) avec visibilité accrue dans les tâches prioritaires et l'administration.
    - Amélioration du processus de matching : clarification des salaires (brut vs net) et intégration de WhatsApp (confirmation de téléphone, statut de réponse et gestion du consentement).
    - Ajout de filtres pour identifier les employeurs ayant répondu.
- **Candidatures Spontanées :**
    - Mise en place d'un workflow complet pour les candidatures spontanées : suivi des candidats et des employeurs, et envoi d'emails d'approche automatisés.
- **Gestion des Invitations :**
    - Ajout d'un nouveau canal d'invitation manuel pour France Travail.
    - Amélioration de la fiabilité des envois groupés et nettoyage des invitations en doublon.

### Évolutions techniques
- **Analytics et Tracking :**
    - Implémentation d'un système de suivi des visites pour Match Europe, avec stockage des données directement dans Grist et analyse détaillée par page.
    - Restauration et amélioration des outils de reporting et d'analytics (FAGERH).
- **Infrastructure et Fiabilité :**
    - Mise en place de scripts de déploiement sécurisés ("guarded deploy scripts").
    - Ajout d'une garde de régression pour sécuriser les fonctionnalités EURES.
    - Optimisation de la gestion des URLs publiques pour les liens magiques d'administration et les tests d'emails.
    - Amélioration de la gestion des doublons de réponses dans le système.

### Autres changements
- Mise à jour de la documentation du journal de projet (incluant les candidatures spontanées et les actualités sur l'IA de recrutement).
