## Changelog : grist-custom-forms (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de l'identité visuelle du projet, avec le rebranding des pages EURES vers "Match Europe". Le projet a également introduit une gestion complète des candidatures spontanées (prospection et suivi) et a bénéficié d'une refonte importante de l'interface d'administration pour améliorer l'efficacité du matching et la lisibilité des données.

### Évolutions fonctionnelles
- **Rebranding et Identité** : Passage de l'identité visuelle des pages EURES vers la marque "Match Europe".
- **Gestion des candidatures spontanées** : Mise en place d'un nouveau flux complet incluant l'envoi d'e-mails de prospection (candidats et employeurs), le suivi des candidatures et la capture automatique des réponses des employeurs.
- **Optimisation de l'administration EURES** : 
    - Refonte globale de l'interface d'administration Match Europe.
    - Amélioration de la lisibilité des listes de matching et des données de relations.
    - Clarification des badges de statut et des notions de salaire (brut vs net).
    - Amélioration des outils de décision de matching manuel.
- **Amélioration du Matching** : 
    - Ajout de filtres (ex: employeur ayant répondu).
    - Meilleure gestion des doublons de réponses EURES.
    - Amélioration du suivi des cas de "non-match".
- **Communication et WhatsApp** : 
    - Ajout de la confirmation de numéro de téléphone WhatsApp pour les employeurs.
    - Affichage du statut WhatsApp des employeurs directement dans les listes de matching.
- **Gestion des invitations** : Ajout d'un canal d'invitation manuel pour France Travail et possibilité de nettoyer les invitations en doublon.
- **Restauration de fonctionnalités** : Réactivation des pages du journal de projet public, des outils de suivi de projet EURES et des rapports d'analyse FAGERH.

### Évolutions techniques
- **Infrastructure et Déploiement** : 
    - Sécurisation des scripts de déploiement (guarded deploy scripts).
    - Mise en place de tests de régression pour EURES.
- **Configuration et Réseau** : 
    - Utilisation d'URLs publiques pour les liens magiques d'administration et les tests d'e-mails.
    - Désactivation des en-têtes de suivi Brevo pour la confidentialité.
- **Performance et Fiabilité** : 
    - Correction d'un problème de timeout lors de l'envoi massif d'invitations.
- **Tests** : Renforcement de la couverture de tests sur les flux d'e-mails (prospection, boutons de réponse, actions de matching).

### Autres changements
- **Documentation** : Mise à jour du journal de projet pour documenter les évolutions de Match Europe et le nouveau processus de candidatures spontanées.
