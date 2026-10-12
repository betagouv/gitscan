## Changelog : st-deploycenter (30 derniers jours, au 02 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur le renforcement des capacités d'administration et de pilotage. L'ajout d'un tableau de bord de métriques et de nouvelles permissions permet une gestion plus fine des opérateurs, tandis que des améliorations d'interface et de gestion des droits fluidifient l'expérience utilisateur.

### Évolutions fonctionnelles
- **Pilotage et administration** :
    - Ajout d'un tableau de bord de métriques pour le suivi des opérateurs.
    - Introduction de la permission `can_admin_operators` pour une gestion accrue des rôles.
    - Amélioration de la résolution des droits (entitlements) pour l'annuaire des collectivités.
- **Expérience utilisateur et API** :
    - Affichage des codes postaux dans les listes déroulantes des communes pour faciliter la saisie.
    - Extension de l'utilisation des clés d'API externes sur plusieurs points de terminaison (endpoints) opérateurs.
    - Correction de la gestion des emails pour les administrateurs d'organisation (la correspondance est désormais insensible à la casse).

### Évolutions techniques
- **Infrastructure et services** :
    - Intégration du service BAL.
    - Optimisation des scripts de liste blanche (allowlist) pour Proconnect.
- **Maintenance et corrections** :
    - Mise à jour du kit d'interface utilisateur (UI Kit).
    - Correction d'un problème de cache lors de la vérification DNS.
    - Régénération du fichier de verrouillage (lockfile) pour assurer la stabilité des déploiements.
