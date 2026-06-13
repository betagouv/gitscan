## Changelog : seves (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, Sèves a bénéficié d'améliorations significatives en termes d'intégration avec Mastro, de l'expérience utilisateur avec l'implémentation de nouveaux filtres (notamment avec Treeselect) et de corrections de bugs pour améliorer la stabilité et la fiabilité de l'application. Des optimisations de performance et des mises à jour de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Intégration finalisée avec Mastro, permettant une meilleure synchronisation des données. [#1010cb5](https://github.com/betagouv/seves/commit/1010cb5)
- Implémentation d'un nouveau filtre Treeselect pour les événements dans le module SSA (Schémas Sanitaires d'Analyse). [#2038](https://github.com/betagouv/seves/commit/8101a61)
- Nouveau Treeselect pour l'investigation des cas humains (SSA). [#0283c1d](https://github.com/betagouv/seves/commit/0283c1d)
- Possibilité de sélectionner une date lors de l'envoi d'un message de note. [#56c2f46](https://github.com/betagouv/seves/commit/56c2f46)
- Ajout du champ "organisme nuisible" dans le module SV (Surveillance Vétérinaire). [#a0ffe42](https://github.com/betagouv/seves/commit/a0ffe42)
- Amélioration de l'affichage des cases à cocher après la mise à jour de django-dsfr. [#732a4ba](https://github.com/betagouv/seves/commit/732a4ba)
- Possibilité de voir les sous-objets ajoutés dans la même révision. [#db94f0b](https://github.com/betagouv/seves/commit/db94f0b)
- Adaptation des exports Europhyt dans le module SV. [#2cb9cc7](https://github.com/betagouv/seves/commit/2cb9cc7)
- Affichage correct des sauts de ligne dans les commentaires de FicheZoneDelimitee et FicheDetection. [#41e51dc](https://github.com/betagouv/seves/commit/41e51dc)

### Évolutions techniques
- Réduction de la taille des instances Scalingo pour optimiser les coûts. [#c6a9665](https://github.com/betagouv/seves/commit/c6a9665)
- Refactorisation du formset `lieux` dans le module SV. [#a283a18](https://github.com/betagouv/seves/commit/a283a18)
- Isolation du filtre Treeselect legacy pour les événements en préparation de la nouvelle implémentation. [#f924d49](https://github.com/betagouv/seves/commit/f924d49)
- Amélioration des performances du bloc commun. [#007ff4d](https://github.com/betagouv/seves/commit/007ff4d)
- Amélioration de la fiabilité des tests, notamment pour les documents et la page d'administration. [#31e1fbc](https://github.com/betagouv/seves/commit/31e1fbc), [#531e4a5](https://github.com/betagouv/seves/commit/531e4a5), [#8857987](https://github.com/betagouv/seves/commit/8857987)
- Mise à jour de plusieurs dépendances : django-dsfr (3.4.2 -> 3.5.1), redis (7.4.0 -> 8.0.0), sentry-sdk (2.59.0 -> 2.61.1), pytest-rerunfailures (16.1 -> 16.3), pytest-playwright (0.7.2 -> 0.8.0), idna (3.7 -> 3.15), playwright (1.59.0 -> 1.60.0), django-reversion (6.1.0 -> 6.2.0), ruff (0.15.12 -> 0.15.16), beautifulsoup4 (4.14.3 -> 4.15.0), django (6.0.5 -> 6.0.6).

### Autres changements
- Ajout d'un avertissement dans le README.md concernant l'utilisation d'un merge-commit pour la MEP. [#2030](https://github.com/betagouv/seves/commit/b0bb6ee) et [#1129581](https://github.com/betagouv/seves/commit/1129581)
- Correction d'une vulnérabilité XSS potentielle dans le numéro de rappel conso. [#306b5c1](https://github.com/betagouv/seves/commit/306b5c1)
- Exclusion du document de la structure MUS lors de l'envoi de notifications. [#4c14041](https://github.com/betagouv/seves/commit/4c14041)
- Amélioration du nommage dans les tests. [#9b2b3f0](https://github.com/betagouv/seves/commit/9b2b3f0)
- Correction d'une régression sur EvenementProduitForm.produit_pret_a_manger avec le nouveau Treeselect. [#c8bc916](https://github.com/betagouv/seves/commit/c8bc916)
- Ajout d'un webhook pour notifier Maestro. [#3c50a2c](https://github.com/betagouv/seves/commit/3c50a2c)
- Changement de l'URL de l'API BAN. [#5bf3107](https://github.com/betagouv/seves/commit/5bf3107)
- Correction d'un problème avec l'édition de la valeur et l'annulation dans TIAC Etablissement. [#767565e](https://github.com/betagouv/seves/commit/767565e)
- Correction de l'alignement du filtre `with_free_links` sur SSA et TIAC. [#7d95473](https://github.com/betagouv/seves/commit/7d95473)
- Amélioration de la fiabilité des tests pour le nombre de résultats dans les choix SV. [#0bc3b47](https://github.com/betagouv/seves/commit/0bc3b47)
- Correction d'un test sur SV pour les longs temps de chargement de page. [#583d0c7](https://github.com/betagouv/seves/commit/583d0c7)
- Correction d'un problème d'affichage de certains boutons après la mise à jour de django-dsfr. [#732a4ba](https://github.com/betagouv/seves/commit/732a4ba)
- Amélioration de la page pour donner les droits d'administration. [#29e1913](https://github.com/betagouv/seves/commit/29e1913)
- Correction des valeurs max et date_reception. [#a9ed4a6](https://github.com/betagouv/seves/commit/a9ed4a6)
- Ajout de choicesjs pour le filtre structure sur la page d'administration. [#b31d352](https://github.com/betagouv/seves/commit/b31d352)
- Correction d'un problème avec l'EML mime type. [#7ce4ef8](https://github.com/betagouv/seves/commit/7ce4ef8)
- Amélioration de l'affichage du label complet avec les catégories dans le bouton Treeselect. [#71bf5c3](https://github.com/betagouv/seves/commit/71bf5c3)
- Force update sur la détection lors de l'édition d'une ZoneInfestee. [#63c3040](https://github.com/betagouv/seves/commit/63c3040)
- Suppression d'une limite de 9 caractères sur le numéro RASFF pour SV. [#57251bc](https://github.com/betagouv/seves/commit/57251bc)
- Modification de la valeur par défaut pour nb_sick_persons dans la vue de transformation. [#954a743](https://github.com/betagouv/seves/commit/954a743)
- Ajout d'une notice pour l'enregistrement simple lorsque >= 10 personnes sont malades. [#c7f4e67](https://github.com/betagouv/seves/commit/c7f4e67)
- Correction d'un test pour l'historique du contenu du prélèvement. [#77c92c6](https://github.com/betagouv/seves/commit/77c92c6)
- Correction d'un test pour le nombre de résultats dans les choix SV. [#20d6a7f](https://github.com/betagouv/seves/commit/20d6a7f)
- Suppression d'un avertissement dans les tests de django-widget-tweaks. [#c457d59](https://github.com/betagouv/seves/commit/c457d59)
- Ajout de différentes couleurs pour les accordéons de niveau 2+ dans Treeselect. [#dade33b](https://github.com/betagouv/seves/commit/dade33b)
