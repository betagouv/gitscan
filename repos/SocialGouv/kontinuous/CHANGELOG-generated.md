## Changelog : kontinuous (30 derniers jours)

### Résumé
Cette version apporte des corrections de bugs et des améliorations concernant la gestion des politiques réseau (netpol) pour CNPG, ainsi que des ajustements pour supporter les branches alpha, beta et next dans la persistance. Des corrections mineures et des mises à jour de dépendances ont également été intégrées pour améliorer la stabilité et la réactivité du système.

### Évolutions fonctionnelles
- Correction d'un bug concernant les politiques réseau (netpol) pour CNPG (#867d5d3).
- Ajout du support des branches alpha, beta et next pour la persistance (#247e205).

### Évolutions techniques
- Mise à jour de la version de `rollout-status` (#fce4054).
- Amélioration de la réactivité des Horizontal Pod Autoscalers (HPA) (#db2a123).

### Autres changements
- Correction d'un problème lié à l'image manquante `bitnami/kubectl` (#8b2a499).
- Correction de conventions de persistance (#88a65dc).
- Définition de l'espace de noms par défaut pour CNPG (#b152102).
- Corrections de typos (#6c0cbc8).
- Ajout de valeurs par défaut pour les Pod Disruption Budgets (PDB) (#6abeb0c).
- Amélioration des annotations pour les DaemonSets (#238300d).
- Publication de la version 1.185.3 (#27d53b16).
