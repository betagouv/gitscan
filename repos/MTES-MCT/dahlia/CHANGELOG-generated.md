## Changelog : dahlia (30 derniers jours, au 23 juin 2026)

### Résumé
Le projet Dahlia a connu une période d'activité intense ces 30 derniers jours, avec des améliorations significatives de la fonctionnalité de recherche et de tri, l'ajout de nouvelles fonctionnalités comme le scraping de dossiers et l'intégration du SSO ProConnect, ainsi que des optimisations de l'infrastructure et de la CI/CD. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la recherche et du tri dans les tableaux des pièces et de l'historique [#22](https://github.com/MTES-MCT/dahlia/issues/22).
- Amélioration de la recherche et du tri des dossiers [#19](https://github.com/MTES-MCT/dahlia/issues/19).
- Ajout d'un bandeau d'alerte pour indiquer que l'environnement n'est pas en production [#20](https://github.com/MTES-MCT/dahlia/issues/20).
- Script pour télécharger un fichier et bouton pour rafraîchir le dossier, améliorant l'accessibilité aux dossiers supprimés [#16](https://github.com/MTES-MCT/dahlia/issues/16).
- Intégration du SSO ProConnect pour l'authentification [#7](https://github.com/MTES-MCT/dahlia/issues/7).
- Scraping de tous les types de dossiers avec anonymisation des données [#6](https://github.com/MTES-MCT/dahlia/issues/6).
- Ajout de la colonne "dernier producteur" pour une meilleure identification des sources [#44](https://github.com/MTES-MCT/dahlia/issues/44).
- Ajout de la date de délétion des dossiers [#40](https://github.com/MTES-MCT/dahlia/issues/40).
- Ajout d'un badge "très urgent" pour signaler les dossiers prioritaires [#21](https://github.com/MTES-MCT/dahlia/issues/21).
- Ajout de détails dans les dossiers pour une meilleure information [#13](https://github.com/MTES-MCT/dahlia/issues/13).
- Mise en page améliorée de la page de garde [#49](https://github.com/MTES-MCT/dahlia/issues/49).

### Évolutions techniques
- Mise en place d'une synchronisation nocturne des données [#12](https://github.com/MTES-MCT/dahlia/issues/12).
- Création de releases et déploiement automatisé en production [#17](https://github.com/MTES-MCT/dahlia/issues/17).
- Amélioration de la configuration de Dependabot pour une gestion plus efficace des dépendances [#30](https://github.com/MTES-MCT/dahlia/issues/30) et [#36](https://github.com/MTES-MCT/dahlia/issues/36).
- Correction d'un problème de déconnexion intempestive après authentification [#10](https://github.com/MTES-MCT/dahlia/issues/10).
- Amélioration de la gestion des erreurs temporaires lors du scraping avec un mécanisme de ré-essai [#8](https://github.com/MTES-MCT/dahlia/issues/8).
- Anonymisation du scraping en fonction de l'environnement [#14](https://github.com/MTES-MCT/dahlia/issues/14).
- Correction de l'anonymisation incomplète des données [#11](https://github.com/MTES-MCT/dahlia/issues/11).
- Mise à jour massive des dépendances pour améliorer la sécurité et la performance [#45](https://github.com/MTES-MCT/dahlia/issues/45).
- Surdéfinition de Vite dans la configuration npm pour une meilleure gestion des assets [#46](https://github.com/MTES-MCT/dahlia/issues/46).
- Ajout de permissions dans la CI pour une meilleure sécurité [#48](https://github.com/MTES-MCT/dahlia/issues/48).
- Utilisation de npm comme gestionnaire de package pour Dependabot [#2](https://github.com/MTES-MCT/dahlia/issues/2).

### Autres changements
- Mise à jour de la documentation INVESTIGATION [#37](https://github.com/MTES-MCT/dahlia/issues/37).
- Mise en forme du code avec Prettier et Linter pour améliorer la lisibilité et la maintenabilité [#15](https://github.com/MTES-MCT/dahlia/issues/15).
- Correction d'un problème avec le paramètre 'directory' dans la configuration de Dependabot [#24](https://github.com/MTES-MCT/dahlia/issues/24).
- Amélioration de la gestion du header et des filtres [#23](https://github.com/MTES-MCT/dahlia/issues/23).
- Correction du checkout manquant avant le déploiement [#4](https://github.com/MTES-MCT/dahlia/issues/4).
- Création de la première version de l'application web Dahlia [#1](https://github.com/MTES-MCT/dahlia/issues/1).
