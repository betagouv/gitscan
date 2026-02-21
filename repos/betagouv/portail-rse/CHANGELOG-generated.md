## Changelog : portail-rse (30 derniers jours)

### Résumé
Ce mois-ci, le portail RSE a connu des améliorations significatives, notamment dans la gestion des utilisateurs, des habilitations et des indicateurs RSE. L'interface utilisateur a été affinée, avec l'ajout de nouvelles fonctionnalités pour les conseillers RSE et les entreprises. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Ajout de la possibilité pour un utilisateur de changer sa fonction RSE.
- Les conseillers RSE peuvent devenir propriétaires si aucun propriétaire n'est désigné.
- Amélioration du flux d'invitation et d'inscription pour les utilisateurs invités.
- Ajout d'une page statique ADM et d'une page intercalaire pour le rapport dans le tableau de bord.
- Affichage des badges dans la sélection des tableaux de bord.
- Ajout de la partie conseillers RSE dans le menu d'en-tête.
- Export de l'état conseiller d'un utilisateur vers Brevo et Metabase.
- L'état conseiller RSE peut être vide.
- Modification du formulaire de modification de compte pour la compatibilité CORS.
- Amélioration de l'affichage de la confirmation d'invitation.
- Ajout des indicateurs de C5, C7 et C8, avec leur intégration dans l'export Excel VSME.
- Les indicateurs de C5 sont rendus non applicables pour les entreprises de moins de 50 salariés.
- Correction de l'affichage des boutons radio pour respecter le DSFR.
- Homogénéisation des noms dans les fils d'ariane et ajout de fils manquants.
- Homogénéisation du terme 'accompagnement' et de ses dérivés dans l'interface.

### Évolutions techniques
- Modification du modèle utilisateur et des habilitations.
- Modification du dispatch OIDC lors de la connexion.
- Refactoring de tests : fusion et suppression de tests non pertinents.
- Suppression d'attributs inutilisés et de code redondant.
- Optimisation des requêtes lors de l'export VSME et des calculs de progression grâce à la mise en cache.
- Activation/désactivation du reporting CSP et JS pour améliorer la stabilité de Sentry.
- Modification du modèle entreprise.
- Ajout de valeurs par défaut initiales possibles dans le schéma des indicateurs.

### Autres changements
- Correction de typos et amélioration du wording à plusieurs endroits de l'interface.
- Suppression d'un bloc HTML et du code associé.
- Correction d'un script d'export pour l'origine du département.
- Suppression du badge beta dans l'en-tête des pages.
- Mise à jour de dépendances : sqlparse, pillow, cryptography.
- Ajout de tests pour les habilitations et les entreprises.
- Correction de l'affichage des images manquantes.
- Suppression des tests OIDC sur la CI.
- Correction d'un test.
- Suppression d'une condition inutile.
- Ajout de commentaires et corrections de commentaires existants.
- Factorisation d'une fixture de test.
- Ajout d'un champ total combustibles fossiles.
- Correction d'une balise HTML fermante manquante.
