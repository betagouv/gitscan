## Changelog : dialog (30 derniers jours, au 27/08/2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une refonte visuelle importante avec l'arrivée d'un nouveau tableau de bord et une mise à jour de l'interface (header, footer, navigation). Les capacités cartographiques ont été enrichies par une meilleure gestion des zones de restriction et l'ajout de nouveaux points d'intérêt. L'expérience utilisateur a également été fluidifiée grâce à de meilleures alertes dans les formulaires et un système d'emails plus complet.

### Évolutions fonctionnelles
- **Interface et Navigation** : Mise en place d'un nouveau tableau de bord [#2032], refonte du header [#2016] et extension du footer [#2015], et ajout du lien d'accueil dans le fil d'Ariane (breadcrumb) sur l'ensemble des pages [#2048].
- **Cartographie** : Ajout de points PR sur la carte [#2005], migration des polygones en zones de restriction [#2006] et application de restrictions sur une zone [#1998], ainsi qu'une amélioration de l'interface de tracé libre [#2033].
- **Formulaires et Expérience Utilisateur** : Ajout d'une alerte en cas de modifications non sauvegardées dans les formulaires d'arrêté [#2007], validation immédiate des numéros de rue côté client [#1999] et amélioration de la visibilité des organisations dans les formulaires [#2023, #2037].
- **Communication** : Mise en place d'emails de suivi après abonnement [#2003] et ajout de l'option "répondre à" (reply-to) utilisant l'utilisateur actuel pour les envois d'emails [#2019].
- **Administration** : Ajout d'un bouton dans le back-office pour l'envoi de rapports IGN [#1995].

### Évolutions techniques
- **API** : Amélioration générale de l'API [#2041], ajout de la recherche de réglementation par code ville [#2008] et passage des données JSON de la réglementation de "privé" à "public" [#1997].
- **Données et Synchronisation** : Correction des processus de synchronisation vers Grist [#2002] et la base BDTopo [#2030], et intégration de mesures SOGELINK dans le transformateur Litteralis [#2026].
- **Monitoring et Sécurité** : Optimisation du suivi Matomo avec le tracking des téléchargements [#2004] et la protection des données locales [#2046], et renforcement de la gestion des erreurs (try/catch) pour l'API des organisations [#2050].

### Autres changements
- Amélioration du processus de mise à jour des statuts IGN [#2039].
- Suppression des notifications d'avertissement pour les organisations incomplètes [#2018].
- Correction de l'affichage (padding) pour les exceptions de ville entière [#2021] et du pictogramme de filtre poids lourd sur la carte [#2020].
