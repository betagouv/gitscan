## Changelog : domifa (30 derniers jours, au 30/09/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur via une interface plus claire (couleurs, libellés, affichage des noms) et l'ajout d'indicateurs de suivi essentiels (délais de passage, dates de domiciliation). La fiabilité du système a également été renforcée par une meilleure gestion des envois d'emails et une optimisation des statistiques.

### Évolutions fonctionnelles
- **Interface et Ergonomie** :
    - Amélioration visuelle des titres, des boutons d'accès et des pastilles d'alerte (mise en conformité avec les tokens DSFR).
    - Mise à jour des libellés dans le menu de pilotage [#4277](https://github.com/SocialGouv/domifa/pull/4277).
    - Affichage du nom complet des usagers dans les dossiers, les notes et les listes d'interactions pour une meilleure identification.
- **Suivi et Données** :
    - Ajout de la date de domiciliation.
    - Mise en place de nouveaux indicateurs visuels pour le suivi des délais de passage et des échéances de décision.
    - Correction des calculs sur le formulaire d'inscription initiale.
- **Statistiques et Communication** :
    - Correction et alignement des données statistiques (comptages par région et chiffres globaux) [#4274](https://github.com/SocialGouv/domifa/pull/4274).
    - Correction des modèles (templates) d'emails.

### Évolutions techniques
- **Backend et Sécurité** :
    - Amélioration du suivi des emails grâce au routage basé sur le statut de livraison Brevo.
    - Renforcement de la confidentialité en masquant les données sensibles dans les logs et les événements Sentry.
    - Nettoyage des logs inutiles et des migrations obsolètes.
- **Maintenance et Performance** :
    - Mise à jour de l'environnement de tests vers Jest 30.
    - Optimisation du code via l'utilisation de la bibliothèque `date-fns` et la suppression de champs et packages inutilisés.
    - Migration de la gestion des statistiques publiques vers un nouveau flux de contrôle (control flow).
    - Amélioration de la stabilité de la chaîne de CI (Intégration Continue).

### Autres changements
- Mise à jour de la documentation technique.
