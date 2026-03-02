## Changelog : portail-rse (30 derniers jours)

### Résumé
Ce mois-ci, le portail RSE a bénéficié d'améliorations significatives, notamment l'ajout de nouveaux indicateurs liés aux thématiques C4, C5 et C7 pour le reporting VSME, ainsi que des optimisations de performance pour l'export des données. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, notamment concernant la gestion des utilisateurs, des habilitations et des invitations.

### Évolutions fonctionnelles
- Ajout des indicateurs de C4, C5 et C7 pour le reporting VSME.
- Les indicateurs de C5 sont désormais marqués comme non applicables pour les entreprises de moins de 50 salariés.
- Amélioration du flux d'invitation et de l'inscription des utilisateurs.
- Ajout de la partie conseillers RSE dans le menu d'en-tête.
- Possibilité pour un utilisateur de changer sa fonction RSE.
- Export de l'état "conseiller" d'un utilisateur vers Metabase.
- Amélioration de la visibilité de l'état "conseiller" des utilisateurs dans l'administration.
- Modification du formulaire de modification de compte pour la compatibilité CORS.
- Ajout d'images manquantes dans l'interface utilisateur.
- Affichage simplifié de la confirmation d'invitation.
- Ajout de badges dans la sélection des tableaux de bord.
- Correction de l'export des indicateurs dans le bon onglet du fichier Excel.
- Suppression du badge "beta" dans l'en-tête des pages.

### Évolutions techniques
- Optimisation de l'export Excel VSME en réduisant le nombre de requêtes à la base de données et en mettant en cache des propriétés du rapport.
- Refactorisation du code pour éviter la duplication et simplifier la logique.
- Amélioration de la gestion des erreurs JavaScript en désactivant temporairement le reporting CSP et JS (réactivable via variable d'environnement).
- Modification du modèle d'habilitation et d'entreprise.
- Modification du dispatch OIDC pour une meilleure gestion de l'authentification.
- Suppression d'une contrainte liée au rôle de propriétaire.
- Amélioration des tests unitaires et suppression de tests non pertinents.
- Utilisation d'un template dédié pour l'invitation d'un propriétaire.
- Correction d'un script d'export pour l'origine du département.
- Suppression d'un bloc HTML et du code associé.

### Autres changements
- Corrections de commentaires et de typographie.
- Homogénéisation des icônes sur les boutons.
- Utilisation du terme "accompagnement" et de ses dérivés dans l'interface.
- Suppression d'un attribut inutilisé.
- Factorisation d'une fixture de test.
- Correction d'un test unitaire.
- Suppression d'une condition inutile.
- Mise à jour de dépendances : sqlparse (0.5.3 -> 0.5.4), pillow (12.1.0 -> 12.1.1), cryptography (46.0.3 -> 46.0.5).
