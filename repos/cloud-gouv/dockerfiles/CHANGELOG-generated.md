## Changelog : dockerfiles (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les mises à jour se concentrent sur l'amélioration de la sécurité des images Docker, notamment pour les jobs GitLab, en intégrant l'outil `debsecan` pour la détection de vulnérabilités dans les paquets Debian.

### Évolutions fonctionnelles
- Ajout de l'outil `debsecan` aux jobs GitLab pour la détection de vulnérabilités des paquets Debian. [#38](https://github.com/cloud-gouv/dockerfiles/issues/38)

### Évolutions techniques
- Intégration de `debsecan` dans le processus de construction des images Docker pour les jobs GitLab.

### Autres changements
- Aucun changement significatif à signaler.
