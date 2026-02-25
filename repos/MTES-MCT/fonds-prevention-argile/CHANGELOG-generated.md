## Changelog : fonds-prevention-argile (30 derniers jours)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives concernant la gestion des allers-vers, l'espace Agent et l'espace AMO (Autorité Maitre d'Oeuvre). Des corrections ont également été apportées pour améliorer la stabilité et la qualité de l'expérience utilisateur, notamment au niveau de la simulation et de l'envoi d'emails.

### Évolutions fonctionnelles
- Ajout de l'éligibilité pour les allers-vers (#140).
- Implémentation du flow d'archivage des AMO (#139).
- Mise à jour des designs de l'AMO (#138).
- Possibilité d'éditer les données de simulation (#137).
- Ajout du code départemental à la liste des allers-vers dans l'espace administrateur (#136).
- Ajout d'un espace Agent pour la gestion des allers-vers (#129).
- Amélioration de la gestion des commentaires (#133).
- Mise à jour des libellés et des données dans l'espace AMO (#124).
- Correction d'un bug concernant les revenus dans la simulation (#123).

### Évolutions techniques
- Doublement du nombre de communes par département pour une meilleure précision géographique (#134).
- Correction d'un problème de redirection dans l'iframe de simulation (#125).
- Correction d'un bug lié à l'iframe et aux données de simulation (#128).
- Mise à jour de la version de Node et du buildpack pour améliorer la sécurité et la performance (#128).
- Application d'un mode "white mode" forcé et suppression du paramètre d'affichage du footer (#131).

### Autres changements
- Corrections diverses de l'interface utilisateur et de commentaires (#135).
- Correction de bugs liés à l'envoi d'emails (mailto) (#126, #127).
- Amélioration de la qualité (QA) des allers-vers (#130).
- Implémentation du back-office AMO suite (#120).
