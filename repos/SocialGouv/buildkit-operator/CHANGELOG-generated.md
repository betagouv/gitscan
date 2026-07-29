## Changelog : buildkit-operator (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, l'opérateur buildkit a bénéficié d'améliorations significatives en matière de gestion du cache S3, de dimensionnement automatique des ressources et de support de nouveaux environnements de construction, notamment avec l'ajout d'un backend local basé sur Incus et ZFS. Ces améliorations visent à optimiser les performances, la fiabilité et la flexibilité de l'opérateur.

### Évolutions fonctionnelles
- Ajout d'une politique de cache "cold" pour S3 : importation toujours activée, exportation périodique, permettant une gestion plus fine des coûts et des performances du cache.
- Possibilité de définir des valeurs par défaut pour les projets lors de leur création, simplifiant la configuration.
- Mise en place d'un dimensionnement adaptatif du cache, ajustant automatiquement la taille en fonction de la cadence de construction.
- Ajout d'un support expérimental pour un backend local basé sur Incus et ZFS, offrant une alternative à Kubernetes pour les environnements de développement ou de test.
- Amélioration de la gestion des références GitLab, permettant de faire confiance aux références du même projet par défaut.
- Implémentation d'un mécanisme de nettoyage (lifecycle GC) des buckets S3 via un job hook, optimisant les coûts de stockage.

### Évolutions techniques
- Renforcement de la robustesse de la gestion du cache S3 après une revue de sécurité.
- Correction d'un problème de compteur inflight qui pouvait croître indéfiniment dans le contrôleur.
- Refactorisation du code pour introduire une interface `Provisioner` pour les backends, facilitant l'ajout de nouveaux supports.
- Mise à jour des actions GitHub pour utiliser Node 24.
- Amélioration des tests unitaires pour maintenir une couverture de code supérieure à 85%.
- Correction de problèmes liés au démarrage des VMs dans le backend local.
- Amélioration de la gestion des erreurs lors de l'exportation du cache S3.

### Autres changements
- Documentation mise à jour pour refléter le support du backend Incus/ZFS.
- Suppression des artefacts de construction locaux du fichier `.gitignore`.
- Ajout de scripts de démarrage rapide pour tester le backend local sur des environnements cloud (OVH/Ubuntu).
- Correction de la gestion des probes de readiness pour le buildkitd.
- Amélioration de la gestion des secrets lors de l'utilisation des actions de construction sur différentes plateformes (GitHub, Forgejo, GitLab).
