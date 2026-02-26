## Changelog : portail-rse (30 derniers jours)

### Résumé
Ce mois-ci, le portail RSE a connu des améliorations significatives concernant l'export des données, notamment pour les indicateurs des cadres C4, C5, C7 et C8. Des corrections et des ajustements ont été apportés à l'interface utilisateur, aux habilitations et à la gestion des utilisateurs. Plusieurs refactorisations techniques ont également été réalisées pour optimiser les performances et la maintenance du code.

### Évolutions fonctionnelles
- Ajout des indicateurs de C4, C5, C7 et C8 et intégration de leur export dans le fichier Excel VSME.
- Amélioration de l'export des données, notamment pour les indicateurs d'origine départementale.
- Possibilité pour un conseiller RSE de devenir propriétaire si aucun propriétaire n'est défini.
- L'état du conseiller RSE est maintenant exportable et visible dans le menu.
- Amélioration de l'expérience utilisateur concernant la sélection des tableaux de bord et l'affichage des badges.
- Ajout d'une page statique ADM et d'une page intercalaire pour le rapport dans le tableau de bord.
- Possibilité pour un utilisateur de modifier sa fonction RSE.
- Modification du flux d'invitation pour une meilleure expérience utilisateur.
- Correction de l'affichage du texte "None" sous les labels des tableaux.
- Correction de l'affichage des indicateurs non pertinents dans les tableaux.
- Désactivation des boutons d'ajout et suppression de ligne lorsque l'indicateur est coché comme non pertinent.
- Rétablissement du label et de la description sur les champs de type auto\_id.
- Correction de l'onglet C4 du template d'export excel VSME.
- Correction du fonctionnement d'un champ auto\_id dans un tableau d'un indicateur non pertinent.
- Correction de l'export des indicateurs dans le bon onglet du fichier excel.
- Correction de la lecture des données d'un indicateur pour ne pas modifier les données brutes.

### Évolutions techniques
- Refactorisation du code pour éviter la duplication et améliorer la lisibilité.
- Optimisation des requêtes en base de données lors de l'export des données VSME et du calcul de la progression.
- Mise en cache de certaines propriétés pour améliorer les performances.
- Activation/désactivation du reporting CSP et JS pour optimiser l'utilisation de Sentry.
- Modification du dispatch OIDC pour une meilleure gestion de l'authentification.
- Modification du modèle d'habilitation et d'utilisateur.
- Suppression de code inutile et de conditions redondantes.
- Amélioration des tests et suppression des tests non pertinents.
- Correction de problèmes CORS en local.
- Ajout d'une valeur par défaut initiale possible dans le schema des indicateurs.

### Autres changements
- Mise à jour des dépendances : sqlparse, pillow, cryptography.
- Amélioration de la documentation et des commentaires.
- Modifications de wording et d'icônes pour une meilleure cohérence.
- Suppression du badge beta dans l'en-tête des pages.
- Suppression d'un bloc HTML et du code associé.
- Homogénéisation des noms dans les fils d'ariane et ajout de fils manquants.
- Correction de typos et d'erreurs de description.
- Ajout d'un lien et de guillemets sur l'explication de non applicabilité.
- Suppression d'une contrainte liée au rôle propriétaire.
- Suppression de la colonne propriétaires du tableau des entreprises accompagnées.
- Remplacement du statut de l'entreprise par le nombre de propriétaires.
- Suppression du statut de l'entreprise lors d'un nouvel accompagnement.
- Suppression d'un attribut inutilisé.
- Inversion de l'ordre des blocs "Anticiper" et "Gérer".
- Correction d'un test.
- Ajout de tests pour les habilitations et les entreprises.
- Correction de l'état conseiller lors de l'enregistrement de l'habilitation.
- Utilisation du template dédié à l'invitation d'un propriétaire.
- Correction d'un wording.
- Ajout de tests.
- Correction de l'importation des tests.
- Correction d'un test.
- Suppression d'une condition inutile.
- Ajout de commentaires.
- Factorisation d'une fixture.
