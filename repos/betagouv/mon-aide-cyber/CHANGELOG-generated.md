## Changelog : mon-aide-cyber (30 derniers jours, au 02/11/2026)

### Résumé
Les récentes évolutions se concentrent sur l'optimisation du parcours de diagnostic RECYF. Le contenu a été considérablement enrichi pour couvrir de nouveaux aspects de la cybersécurité (gestion des accès, sécurité des postes, gouvernance) et simplifié par la suppression d'éléments obsolètes, tout en améliorant la clarté des aides à la saisie pour les utilisateurs.

### Évolutions fonctionnelles
- Mise à jour approfondie du diagnostic RECYF :
    - Ajout de nouvelles questions sur la gestion des accès (comptes à privilèges, complexité des mots de passe, accès distants, télétravail), la sécurité des postes (antivirus, mises à jour, cloisonnement des systèmes) et la gouvernance (contrats prestataires, suivi des vulnérabilités, schémas des SI).
    - Renforcement du volet "Réaction" (gestion de crise, restauration des sauvegardes, liste des contacts d'urgence).
    - Simplification du parcours par la suppression de thématiques et de questions devenues obsolètes.
    - Optimisation de l'expérience utilisateur : correction de libellés, réorganisation de l'ordre des questions et amélioration de la clarté des info-bulles d'aide.
- Corrections de navigation et d'affichage :
    - Correction de l'affichage des articles CRISP.
    - Mise à jour de l'URL MSC pour rediriger correctement vers la nouvelle page de demande de diagnostic.

### Évolutions techniques
- Sécurité et infrastructure :
    - Mise à jour de la version de Node.js.
    - Mise à jour de l'outil `pnpm` au sein de la chaîne de CI/CD.
- Maintenance du code :
    - Correction du typage TypeScript suite à la montée de version de la bibliothèque Knex.
