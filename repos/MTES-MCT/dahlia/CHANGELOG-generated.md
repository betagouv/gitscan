## Changelog : dahlia (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'application Dahlia a connu des améliorations significatives en termes de fonctionnalités, notamment l'ajout du scrapping automatisé des dossiers, l'amélioration de la recherche et du tri, ainsi que l'intégration de l'authentification SSO ProConnect. Des efforts importants ont également été consacrés à l'amélioration de la stabilité et de la maintenance du projet, avec des mises à jour de dépendances et une configuration optimisée de Dependabot.

### Évolutions fonctionnelles
- **Scrapping et gestion des pièces :** Amélioration du scrapping des données et ajout de la possibilité d'éditer les pièces d'un dossier [#50](https://github.com/MTES-MCT/dahlia/issues/50).
- **Recherche et tri :** Ajout de la recherche et du tri dans les tableaux des pièces et de l'historique [#22](https://github.com/MTES-MCT/dahlia/issues/22) et amélioration de la recherche et du tri des dossiers [#19](https://github.com/MTES-MCT/dahlia/issues/19).
- **Authentification :** Intégration de l'authentification SSO ProConnect [#7](https://github.com/MTES-MCT/dahlia/issues/7).
- **Gestion des dossiers :** Ajout de la possibilité de télécharger un fichier, d'un bouton pour rafraîchir le dossier et amélioration de l'accessibilité des dossiers supprimés [#16](https://github.com/MTES-MCT/dahlia/issues/16).
- **Informations dossier :** Ajout de détails supplémentaires dans les dossiers [#13](https://github.com/MTES-MCT/dahlia/issues/13).
- **Interface utilisateur :** Mise en page de la page de garde [#49](https://github.com/MTES-MCT/dahlia/issues/49), ajout d'un bandeau indiquant l'environnement (non-production) [#20](https://github.com/MTES-MCT/dahlia/issues/20) et ajout d'un badge "très urgent" [#21](https://github.com/MTES-MCT/dahlia/issues/21).
- **Synchronisation :** Ajout d'une synchronisation nocturne des données [#12](https://github.com/MTES-MCT/dahlia/issues/12).

### Évolutions techniques
- **CI/CD :** Ajout de permissions dans la CI [#48](https://github.com/MTES-MCT/dahlia/issues/48) et ajout de la création de release et du déploiement en production [#17](https://github.com/MTES-MCT/dahlia/issues/17).
- **Dependabot :** Amélioration de la configuration de Dependabot [#30](https://github.com/MTES-MCT/dahlia/issues/30) et amélioration de Dependabot pour gérer les mises à jour de dépendances [#36](https://github.com/MTES-MCT/dahlia/issues/36).
- **Scrapping :** Anonymisation du scrapping selon l'environnement [#14](https://github.com/MTES-MCT/dahlia/issues/14) et ajout d'un mécanisme de ré-essai en cas d'erreurs temporaires lors du scrapping [#8](https://github.com/MTES-MCT/dahlia/issues/8).
- **Configuration :** Surdéfinition de `vite` dans la configuration npm [#46](https://github.com/MTES-MCT/dahlia/issues/46).
- **Divers :** Ajout de la colonne "dernier producteur" [#44](https://github.com/MTES-MCT/dahlia/issues/44) et ajout de la date de délétion [#40](https://github.com/MTES-MCT/dahlia/issues/40).

### Autres changements
- Mise à jour de la documentation INVESTIGATION [#37](https://github.com/MTES-MCT/dahlia/issues/37).
- Correction d'un problème où le lien de déconnexion déconnectait l'utilisateur immédiatement après la connexion [#10](https://github.com/MTES-MCT/dahlia/issues/10).
- Correction d'un problème d'anonymisation incomplète [#11](https://github.com/MTES-MCT/dahlia/issues/11).
- Mise à jour massive des dépendances [#45](https://github.com/MTES-MCT/dahlia/issues/45) et mises à jour de dépendances spécifiques (prettier, eslint-config-next, @codegouvfr/react-dsfr, next, better-auth, tailwindcss, @tailwindcss/postcss) [#25](https://github.com/MTES-MCT/dahlia/issues/25), [#27](https://github.com/MTES-MCT/dahlia/issues/27), [#28](https://github.com/MTES-MCT/dahlia/issues/28), [#29](https://github.com/MTES-MCT/dahlia/issues/29), [#33](https://github.com/MTES-MCT/dahlia/issues/33), [#35](https://github.com/MTES-MCT/dahlia/issues/35), [#39](https://github.com/MTES-MCT/dahlia/issues/39), [#41](https://github.com/MTES-MCT/dahlia/issues/41), [#42](https://github.com/MTES-MCT/dahlia/issues/42), [#43](https://github.com/MTES-MCT/dahlia/issues/43).
- Mise en forme du code avec Prettier et Linter [#15](https://github.com/MTES-MCT/dahlia/issues/15).
- Correction d'un bug dans la configuration de Dependabot [#24](https://github.com/MTES-MCT/dahlia/issues/24).
- Correction d'un problème de checkout avant le déploiement [#4](https://github.com/MTES-MCT/dahlia/issues/4).
