## Changelog : domifa (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois-ci, domifa a bénéficié d'améliorations significatives pour faciliter le suivi des usagers, notamment via de nouveaux indicateurs de délais et une meilleure gestion des dates de domiciliation. L'expérience de navigation a été simplifiée pour les agents de pilotage, et la sécurité des données a été renforcée lors des modifications de profil.

### Évolutions fonctionnelles
- **Suivi des usagers :** Ajout de la gestion de la date de domiciliation et mise en place d'indicateurs visuels (pastilles de couleur) pour suivre les délais de passage et de décision.
- **Clarté de l'interface :** Amélioration de l'identification des usagers dans les dossiers et les listes d'interaction grâce à l'affichage systématique du nom complet.
- **Navigation et accès :** 
    - Remplacement du menu "Administration" par "Pilotage" dans la barre de navigation [#4277](https://github.com/SocialGouv/domifa/pull/4277).
    - Redirection automatique des profils spécifiques (DGCS, DDETS, DREETS) vers le portail de pilotage lors de la connexion.
- **Nouveaux outils :** Ajout d'un formulaire de contact pour le support et intégration d'un onglet "Kit de communication" incluant une section FAQ [#4270](https://github.com/SocialGouv/domifa/pull/4270).
- **Statistiques :** Corrections de l'affichage (CSS) et de la précision des chiffres dans les tableaux de bord statistiques [#4274](https://github.com/SocialGouv/domifa/pull/4274).

### Évolutions techniques
- **Sécurité :** Renforcement du processus de mise à jour des adresses email (frontend et backend).
- **Gestion des communications :** Amélioration du suivi des envois d'emails via la synchronisation des statuts de livraison Brevo.
- **Maintenance et performance :**
    - Optimisation de la confidentialité par le nettoyage des logs (Sentry et logs HTTP redigés).
    - Allègement du backend par la suppression de Swagger et de migrations obsolètes.
    - Mise à jour de l'environnement de test (passage à Jest 30).
- **Refactoring :** Amélioration de la validation des données (DTO) côté backend et adoption de la bibliothèque `date-fns` pour la gestion des dates.

### Autres changements
- **Contenu :** Mise à jour des composants et des textes des pages publiques (FAQ, impact, témoignages, actualités).
- **Nettoyage :** Suppression de champs de données inutilisés et de packages obsolètes.
