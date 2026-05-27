## Changelog : seves (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment avec l'implémentation d'un nouveau composant de sélection arborescente (Treeselect) et l'ajout de cartes pour la localisation des lieux d'investigation. Des corrections de sécurité importantes ont également été apportées, ainsi que des améliorations de la gestion des documents et des exports de données.

### Évolutions fonctionnelles
- Ajout d'une carte pour visualiser les lieux lors de la création d'une investigation SV.
- Amélioration de l'affichage des informations sur les sites d'inspection dans SV, avec l'ajout de blocs dédiés aux lieux, aux prélèvements et aux éléments infestés.
- Implémentation d'un nouveau composant Treeselect pour la sélection d'éléments dans SSA, améliorant l'expérience utilisateur.
- Possibilité de télécharger les documents associés à une investigation dans une archive ZIP.
- Ajout d'un champ obligatoire pour le nombre de personnes malades lors d'une investigation TIAC.
- Amélioration de l'affichage des retours à la ligne dans les messages.
- Correction d'un problème d'affichage des PDF dans le navigateur Brave.
- Ajout d'une page d'accessibilité.
- Ajout de la possibilité de télécharger des documents même sans date de publication.
- Ajout de l'ON (Organisme Notifié) pour SV.
- Amélioration de l'historique des investigations SV.

### Évolutions techniques
- Correction d'une vulnérabilité XSS potentielle liée au numéro de rappel conso.
- Refactorisation du code pour améliorer la fiabilité des tests, notamment pour les SV et les pages d'administration.
- Suppression des feature flags pour l'éditeur de texte enrichi et le téléchargement en ZIP.
- Migration du modèle SiteInspection vers un choix de texte (TextChoices).
- Amélioration de la performance des tests.
- Modification de l'approche de mise à jour des SV pour une meilleure efficacité.
- Correction d'un conflit de migration entre les migrations 0121_lieu_site_inspection_new et 0121_add_on_phytophthora_kernoviae.
- Ajout d'un webhook pour notifier Maestro.
- Modification de l'URL de l'API BAN.
- Amélioration de la gestion des dates dans SV pour assurer la cohérence des fuseaux horaires.
- Modification de l'ordre par défaut des TIAC et Alim.
- Correction de problèmes liés à l'utilisation de l'API ChoiceJSPage.

### Autres changements
- Mise à jour de plusieurs dépendances : Ruff, pytest-rerunfailures, pytest-playwright, sentry-sdk, idna, playwright, django-reversion, gunicorn, psycopg2-binary, pre-commit.
- Nettoyage du code et amélioration de la documentation.
- Correction de problèmes de compatibilité avec certains navigateurs (Brave/Chromium).
- Amélioration du format d'export CSV pour TIAC.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Correction d'un problème de tooltip sur TIAC.
- Suppression des avertissements Python sur CI pour améliorer la lisibilité.
