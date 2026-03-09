## Changelog : portail-rse (30 derniers jours)

### Résumé
Ce mois-ci, le portail RSE a connu des améliorations significatives, notamment autour de la gestion des utilisateurs et de leur rôle (conseiller RSE, propriétaire), ainsi que de l'intégration avec Proconnect pour une meilleure expérience de connexion et d'invitation. Des améliorations ont également été apportées à l'export des données VSME, notamment avec l'ajout des indicateurs C4 et C7, et des optimisations de performance pour réduire le temps de génération des exports.

### Évolutions fonctionnelles
- Amélioration du processus d'invitation via Proconnect : acceptation automatique de l'invitation en arrivant sur l'URL, simplification de la cinématique d'invitation.
- Les utilisateurs connectés via Proconnect peuvent désormais modifier leur compte.
- Possibilité pour un utilisateur de changer sa fonction RSE (conseiller ou non).
- Ajout des indicateurs C4 et C7 et de leur exportation dans le fichier Excel VSME.
- Les entreprises accompagnées peuvent avoir plusieurs propriétaires.
- Amélioration de l'affichage des badges dans la sélection des tableaux de bord.
- Ajout de la partie conseillers RSE dans le menu d'en-tête.
- Modification du flux d'inscription pour les invitations.
- Précisions dans la documentation concernant les e-mails à utiliser en recette avec ProConnect.
- Suppression du statut de l'entreprise lors d'un nouvel accompagnement.
- Amélioration du wording (terminologie) pour une meilleure clarté.

### Évolutions techniques
- Refactorisation du code pour simplifier la redirection Proconnect et l'initialisation des variables.
- Optimisation des requêtes lors de l'export des données VSME pour améliorer les performances.
- Mise en cache de certaines données pour réduire le nombre de requêtes en base de données.
- Modification du modèle utilisateur et entreprise pour supporter les nouvelles fonctionnalités.
- Amélioration de la gestion des erreurs et suppression de certaines erreurs silencieuses.
- Correction de problèmes liés à la session après suppression d'une entreprise.
- Correction de bugs liés à l'affichage et au fonctionnement des champs de formulaire.
- Amélioration des tests et suppression de tests devenus non pertinents.
- Correction d'un problème de CORS empêchant la modification du compte utilisateur.
- Activation/désactivation du reporting CSP et JS pour améliorer la stabilité de Sentry.

### Autres changements
- Mise à jour des dépendances : `joserfc` (1.4.2 -> 1.6.3), `sqlparse` (0.5.3 -> 0.5.4), `pillow` (12.1.0 -> 12.1.1), `cryptography` (46.0.3 -> 46.0.5).
- Suppression de code inutile et refactorisation de certaines parties du code.
- Amélioration des commentaires et de la documentation.
- Correction de certains tests.
- Suppression du badge beta dans l'en-tête des pages.
