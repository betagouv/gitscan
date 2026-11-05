## Changelog : mon-aide-cyber (30 derniers jours, au 02/11/2026)

### Résumé
Cette période a été marquée par une refonte majeure du diagnostic RECYF. L'objectif a été d'enrichir le contenu de cybersécurité (gouvernance, accès, postes de travail) tout en simplifiant le parcours utilisateur par la suppression de questions obsolètes et l'amélioration de l'aide textuelle (info-bulles).

### Évolutions fonctionnelles
- **Refonte du diagnostic RECYF** :
    - Ajout de nouvelles questions couvrant la gouvernance (contrats prestataires, suivi des vulnérabilités, schémas des SI), la sécurité des accès (comptes à privilèges, complexité des mots de passe, télétravail, accès distants) et la sécurité des postes (antivirus, mises à jour, cloisonnement des systèmes).
    - Renforcement de la partie "Réaction" avec des questions sur la gestion de crise et la restauration des sauvegardes.
    - Intégration de nouveaux éléments de sensibilisation (respect de charte, actions de sensibilisation).
    - Suppression des thématiques et questions devenues obsolètes pour gagner en pertinence.
    - Réintégration des questions relatives au RGPD.
- **Améliorations de l'expérience utilisateur** :
    - Correction et harmonisation des info-bulles et des libellés pour faciliter la compréhension des questions.
    - Correction de l'affichage des articles CRISP.
    - Mise à jour de l'URL MSC pour pointer directement vers la nouvelle page de demande de diagnostic.

### Évolutions techniques
- **Maintenance de l'environnement** :
    - Mise à jour de la version de Node.js.
    - Mise à jour de la version de pnpm dans la chaîne de CI.
- **Qualité et maintenance du code** :
    - Correction du typage suite à la montée de version de la bibliothèque Knex.
    - Optimisation du workflow de maintenance via le regroupement des Pull Requests de mise à jour des dépendances.
