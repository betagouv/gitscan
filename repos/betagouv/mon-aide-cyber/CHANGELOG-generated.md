## Changelog : mon-aide-cyber (30 derniers jours, au 09/11/2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une refonte majeure de son outil de diagnostic pour le rendre plus complet et pertinent, avec l'ajout de nouvelles thématiques de cybersécurité. Parallèlement, des améliorations de sécurité et de stabilité ont été apportées au système pour renforcer la fiabilité du service.

### Évolutions fonctionnelles
- **Refonte du parcours de diagnostic (RECYF) :**
  - Ajout de nouvelles questions couvrant la gouvernance, la gestion des accès (comptes à privilèges, accès distants, télétravail), les sauvegardes et la conformité RGPD.
  - Suppression des thématiques et des questions devenues obsolètes.
  - Réorganisation de l'ordre des questions pour améliorer la fluidité du parcours.
- **Amélioration de l'accompagnement utilisateur :**
  - Mise à jour des libellés et enrichissement des info-bulles d'aide pour clarifier les réponses attendues.
  - Correction de l'affichage des articles CRISP.
  - Correction de l'URL de redirection vers la page de demande de diagnostic.

### Évolutions techniques
- **Sécurité et robustesse :**
  - Mise à jour de la version de Node.js.
  - Amélioration de la gestion et du logging des erreurs (notamment pour la réinitialisation de mot de passe et la gestion des appels Metabase).
  - Correction de typage suite à la montée de version de la bibliothèque Knex.
- **Infrastructure et CI/CD :**
  - Mise à jour de la version de pnpm dans la chaîne d'intégration continue.
