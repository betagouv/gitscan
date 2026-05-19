## Changelog : ma-cantine (30 derniers jours, au 18 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur les achats, notamment au niveau du formulaire de création et de la gestion des caractéristiques. Des corrections ont également été apportées concernant la gestion des données géographiques et la sécurité, ainsi que des optimisations techniques et des ajustements liés à la télédéclaration des bilans.

### Évolutions fonctionnelles
- **Achats :** Le formulaire de création et de modification d'achat a été amélioré en divisant les caractéristiques en quatre sections distinctes, facilitant ainsi la saisie et la gestion des informations. ([#6720](https://github.com/betagouv/ma-cantine/issues/6720))
- **Achats :** Une nouvelle caractéristique "EUROPE" a été ajoutée pour les achats. ([#6708](https://github.com/betagouv/ma-cantine/issues/6708))
- **Bandeau Démo :** Le texte explicatif du bandeau de démonstration a été mis à jour pour plus de clarté. ([#6717](https://github.com/betagouv/ma-cantine/issues/6717))
- **Données Géographiques :** Mise à jour du fichier de référence PAT (Points d'Approvisionnement Territoriaux) pour intégrer les données les plus récentes. ([#6714](https://github.com/betagouv/ma-cantine/issues/6714))
- **Tableau de bord :** Ajout d'un filtre permettant d'afficher les bilans télédéclarés. ([#6655](https://github.com/betagouv/ma-cantine/issues/6655))

### Évolutions techniques
- **Achats :** Ajout de querysets spécifiques pour faciliter l'accès aux achats par utilisateur et par année. ([#6719](https://github.com/betagouv/ma-cantine/issues/6719))
- **Achats :** Regroupement des statistiques d'agrégation dans une queryset dédiée pour améliorer les performances. ([#6706](https://github.com/betagouv/ma-cantine/issues/6706))
- **Achats :** Liste des groupes de caractéristiques pour faciliter leur réutilisation. ([#6702](https://github.com/betagouv/ma-cantine/issues/6702))
- **Modèles :** Réorganisation des champs dans les modèles pour une meilleure lisibilité (Meta et timestamps déplacés en bas). ([#6703](https://github.com/betagouv/ma-cantine/issues/6703))
- **ETL :** Ajout des mesures de gaspillage (WasteMeasurements) aux exports bruts (dbt). ([#6705](https://github.com/betagouv/ma-cantine/issues/6705))
- **Diagnostics :** Amélioration de la commande `diagnostic_fill_invalid_reason_list` (application et récapitulatif des statistiques). ([#6700](https://github.com/betagouv/ma-cantine/issues/6700))
- **API :** Amélioration de l'API pour la validation des données Open Data, en vérifiant la validité des fichiers avant l'export. ([#6713](https://github.com/betagouv/ma-cantine/issues/6713))
- **API :** Rendre l'appel à la fonction d'adresse indépendant de l'objet 'response'. ([#6712](https://github.com/betagouv/ma-cantine/issues/6712))
- **API :** Suppression de l'utilisation de camelCase dans la transformation des résultats de l'API de recherche d'entreprises. ([#6710](https://github.com/betagouv/ma-cantine/issues/6710))
- **Télédéclarations :** Clarification des méthodes pour récupérer les dates de fin de campagne. ([#6657](https://github.com/betagouv/ma-cantine/issues/6657))
- **Télédéclarations :** Simplification du code des règles métiers encadrant la télédéclaration. ([#6656](https://github.com/betagouv/ma-cantine/issues/6656))
- **Télédéclarations :** Suppression du code lié aux anciens imports de bilans. ([#6642](https://github.com/betagouv/ma-cantine/issues/6642))

### Autres changements
- **CGU :** Correction de l'URL vers les Conditions Générales d'Utilisation du frontend. ([#6701](https://github.com/betagouv/ma-cantine/issues/6701))
- **Sécurité :** Sanitize du paramètre 'next' pour prévenir les failles de sécurité. ([#6709](https://github.com/betagouv/ma-cantine/issues/6709))
- **Campagne de correction :** Correction du lien dans le bandeau d'information relatif à la campagne de correction. ([#6675](https://github.com/betagouv/ma-cantine/issues/6675))
- **Télédéclarations :** Correction de l'affichage du pourcentage des valeurs durables et de qualité. ([#6668](https://github.com/betagouv/ma-cantine/issues/6668))
- **Police Marianne :** Correction du problème de non-affichage de la police Marianne. ([#6669](https://github.com/betagouv/ma-cantine/issues/6669))
- **Tableau de bord :** Masquage du message "Non renseignée" pour la colonne 'commune' dans le tableau de bord pour les groupes. ([#6653](https://github.com/betagouv/ma-cantine/issues/6653))
- **Diagnostics :** Ajout d'un filtre pour afficher les télédéclarations générées. ([#6582](https://github.com/betagouv/ma-cantine/issues/6582))
